import asyncio
import aiohttp
import pandas as pd
import nest_asyncio
import warnings
from asyncio import Semaphore
from tqdm.asyncio import tqdm
from io import StringIO 

class InvalidEngineError(Exception):
    """Exception raised when an invalid engine is provided."""
    pass

class InvalidMarketError(Exception):
    """Exception raised when an invalid market is provided for the given engine."""
    pass

class InvalidParametersError(Exception):
    """Exception raised when an parameters is empty for the abstract ISS url."""
    pass

class ISSMOEX:
    """
    A class to interact with the Moscow Exchange (MOEX) ISS (Internet Securities Service) API for fetching 
    various financial data asynchronously.
    
    Attributes:
    ----------
    concurrent_n : int
        Number of concurrent requests allowed.
    engines : pandas.DataFrame
        DataFrame containing the available engines.
    engines_list : list
        List of available engines.
    engines_markets : dict
        Dictionary mapping each engine to its available markets.


    Methods:
    -------
    fetch(session, url, retries=3):
        Fetches the content of the given URL with specified retry attempts.

    fetch_page(session, base_url, start):
        Fetches a specific page of results from the given base URL with a starting record number.

    fetch_all_pages(session, base_url, records_per_page, pages=True):
        Fetches all pages of data from the given base URL.

    fetch_all_data(parameters, url_func, records_per_page=100, pages=True, show_progress=False):
        Fetches all data for the given parameters using the provided URL function.

    fetch_single_page(url):
        Fetches a single page of data from the given URL.

    run_fetcher(coroutine):
        Runs the given coroutine using the event loop.

    bonds_coupons(isin: str, show_progress=True):
        Fetches bond coupon data for the given ISIN(s).

    bonds_amort(isin: str, show_progress=True):
        Fetches bond amortization data for the given ISIN(s).

    securities_market(market: str):
        Fetches securities market data for the given market.

    zyc_params(date: str, show_progress=False):
        Fetches zero-coupon yield curve parameters for the given date(s).

    market_data(engine: str,market: str, isin: str, show_progress=False):
        Fetches market data for the given market and ISIN(s).

    index_components(index: str, date: str, show_progress=False):
        Fetches index components for the given index and date(s).

    history_prices(engine: str,market: str, isin: str, date: str, show_progress=False):
        Fetches historical prices for the given engine, ISIN, and date.

    markets(self,engine): 
        Fetches list of markets for given engine.

    tables_description(self,engine: str, market: str): 
            Fetches description of columns in each possible table for given engine and market.

    indices(self)
            Fetches data abount indices at MOEX.

    iss_url(self,url,parameters = None, pages = False, show_progress = False):
            Fetches data from a specified URL, handling pagination if necessary.

    engine_market_check(self, engine: str, market: str):
            Check if the provided engine and market are valid.
    """
    
    def __init__(self, concurrent_n=10, proxy = None):
        """
        Initializes the ISSas instance with the specified number of concurrent requests.
        
        Parameters:
        ----------
        concurrent_n : int, optional
            Number of concurrent requests allowed (default is 10).
        
        proxy: None 
            proxy of Internet connection
        """
        nest_asyncio.apply()
        self.concurrent_n = concurrent_n
        self.proxy = proxy 

        url = 'https://iss.moex.com/iss/engines.html?iss.only=engines'
        
        coroutine = self.fetch_single_page(url)
        engines = self.run_fetcher(coroutine)
        
        engines.columns = [i.split()[0] for i in engines.columns]
        self.engines = engines
        self.engines_list = engines['name'].to_list()

        url = lambda engine: f'https://iss.moex.com/iss/engines/{engine}/markets.html'
        engines_markets = {}
        for engine in self.engines_list:
            url_market = url(engine)
            coroutine = self.fetch_single_page(url_market)
            market = self.run_fetcher(coroutine)
            markets_names = market[market.columns[1]].to_list()
            engines_markets[engine] = markets_names
        self.engines_markets = engines_markets

    async def fetch(self, session, url, retries=3):
        """
        Fetches the content of the given URL with specified retry attempts.
        
        Parameters:
        ----------
        session : aiohttp.ClientSession
            The session to use for making the request.
        url : str
            The URL to fetch.
        retries : int, optional
            Number of retry attempts in case of failure (default is 3).
            
        Returns:
        -------
        str or None
            The content of the response if successful, None otherwise.
        """
        for attempt in range(retries):
            async with self.semaphore:
                try:
                    await asyncio.sleep(0.1 * (2 ** attempt))  # Exponential backoff starting with 0.1 seconds
                    if self.proxy: 
                        async with session.get(url, proxy = self.proxy) as response:
                            response.raise_for_status()
                            return await response.text()
                    else: 
                        async with session.get(url, proxy = self.proxy) as response:
                            response.raise_for_status()
                            return await response.text()            
                except aiohttp.ClientError as e:
                    print(f"Failed to fetch {url}: {e}")
                    if attempt == retries - 1:
                        return None

    async def fetch_page(self, session, base_url, start):
        """
        Fetches a specific page of results from the given base URL with a starting record number.
        
        Parameters:
        ----------
        session : aiohttp.ClientSession
            The session to use for making the request.
        base_url : str
            The base URL to fetch from.
        start : int
            The starting record number for the page.
            
        Returns:
        -------
        str or None
            The content of the response if successful, None otherwise.
        """
        if base_url[-4:] == 'html':
            url = f"{base_url}?start={start}"

        else:
            url = f"{base_url}&start={start}"
        return await self.fetch(session, url)

    async def fetch_all_pages(self, session, base_url, records_per_page, pages=True):
        """
        Fetches all pages of data from the given base URL.
        
        Parameters:
        ----------
        session : aiohttp.ClientSession
            The session to use for making the request.
        base_url : str
            The base URL to fetch from.
        records_per_page : int
            Number of records per page.
        pages : bool, optional
            Flag to indicate if pagination is required (default is True).
            
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing all the fetched data.
        """
        self.semaphore = Semaphore(self.concurrent_n)
        if not pages:
            html_content = await self.fetch(session, base_url)
            html_content = StringIO(html_content) 
            if html_content:
                return pd.read_html(html_content,encoding= 'utf-8')[0]
            return pd.DataFrame()

        dataframes = []
        start = 0
        while True:
            tasks = [self.fetch_page(session, base_url, start + i * records_per_page) for i in range(3)]
            results = await asyncio.gather(*tasks)
            for html_content in results:
                if html_content is None:
                    continue
                html_content = StringIO(html_content) 
                dfs = pd.read_html(html_content,encoding = 'utf-8')
                if not dfs:
                    return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()
                df = dfs[0]
                if df.empty:
                    return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()
                dataframes.append(df)
                start += records_per_page
        return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()

    async def fetch_all_data(self, parameters, url_func, records_per_page=100, pages=True, show_progress=False):
        """
        Fetches all data for the given parameters using the provided URL function.
        
        Parameters:
        ----------
        parameters : list
            List of parameters to fetch data for.
        url_func : function
            Function that generates the URL for each parameter.
        records_per_page : int, optional
            Number of records per page (default is 100).
        pages : bool, optional
            Flag to indicate if pagination is required (default is True).
        show_progress : bool, optional
            Flag to indicate if progress should be shown (default is False).
        dict: bool, optinonal
            Flag to indicate if return is of dictionary type or list (necessary for getting correct self.engines_markets)
            
        Returns:
        -------
        list of pd.DataFrame
            A list of DataFrames containing the fetched data.
        """
        async with aiohttp.ClientSession(trust_env=True) as session:
            tasks = [self.fetch_all_pages(session, url_func(param), records_per_page, pages) for param in parameters]
            if show_progress:
                tasks_iter = tqdm(asyncio.as_completed(tasks), desc="Fetching data", total=len(tasks))
            else:
                tasks_iter = asyncio.as_completed(tasks)

            results = []
            for task in tasks_iter:
                result = await task
                if result is not None:
                    results.append(result)
            return results
        
    async def fetch_single_page(self, url, records_per_page = 100,pages = False ):
        """
        Fetches a single page of data from the given URL.
        
        Parameters:
        ----------
        url : str
            The URL to fetch.
            
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the fetched data.
        """
        self.semaphore = Semaphore(self.concurrent_n)
        async with aiohttp.ClientSession(trust_env=True) as session:
            result = await self.fetch_all_pages(session, url,records_per_page = records_per_page, pages = pages)
            return result

    def run_fetcher(self, coroutine):
        """
        Runs the given coroutine using the event loop.
        
        Parameters:
        ----------
        coroutine : coroutine
            The coroutine to run.
            
        Returns:
        -------
        Any
            The result of the coroutine.
        """
        try:
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(coroutine)
        except RuntimeError:
            # If no running event loop, create a new one
            return asyncio.run(coroutine)

    def bonds_coupons(self, isin, show_progress=True):
        """
        Fetches bond coupon data for the given ISIN(s).
        
        Parameters:
        ----------
        isin : str or list of str
            The ISIN or list of ISINs to fetch coupon data for.
        show_progress : bool, optional
            Flag to indicate if progress should be shown (default is True).
            
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the bond coupon data.
        """
        isins = [isin] if isinstance(isin, str) else isin
        url_func = lambda isin: f"https://iss.moex.com/iss/statistics/engines/stock/markets/bonds/bondization/{isin}.html?iss.only=coupons"
        coroutine = self.fetch_all_data(parameters=isins, url_func=url_func, show_progress=show_progress, records_per_page=20)
        coupons = self.run_fetcher(coroutine)
 
        coupons = pd.concat(coupons, axis=0)
        coupons.columns = [i.split()[0] for i in coupons.columns]
        cols_datetime = ['coupondate', 'recorddate', 'startdate']
        try:
            coupons[cols_datetime] = coupons[cols_datetime].apply(pd.to_datetime, errors='coerce')
        except KeyError:
            warnings.warn(f"{isin}: empty coupons table")
        return coupons

    def bonds_amort(self, isin, show_progress=True):
        """
        Fetches bond amortization data for the given ISIN(s).
        
        Parameters:
        ----------
        isin : str or list of str
            The ISIN or list of ISINs to fetch amortization data for.
        show_progress : bool, optional
            Flag to indicate if progress should be shown (default is True).
            
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the bond amortization data.
        """
        isins = [isin] if isinstance(isin, str) else isin
        url = lambda isin: f'https://iss.moex.com/iss/statistics/engines/stock/markets/bonds/bondization/{isin}.html?iss.only=amortizations'
        coroutine = self.fetch_all_data(parameters=isins, url_func=url, show_progress=show_progress, records_per_page=20)
        coupons = self.run_fetcher(coroutine)
        
        coupons = pd.concat(coupons, axis=0)
        coupons.columns = [i.split()[0] for i in coupons.columns]
        cols_datetime = ['amortdate']
        try: 
            coupons[cols_datetime] = coupons[cols_datetime].apply(pd.to_datetime, errors='coerce')
        except: 
            warnings.warn(f"{isin}: empty amortization table")
        return coupons
    
    def securities_market(self, engine: str, market: str,main_board = True):
        """
        Fetches securities market data for the given market.
        
        Parameters:
        ----------
        engine : str
            The engine from ISS.
        market : str
            The market of given engine from ISS.
        main_board: bool, optiona; 
            Flag to inficate if the data contains information about main board. 

        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the securities market data.
        """
        self.engine_market_check(engine = engine,market = market)
        main_board = 1 if main_board else 0
        url = f"https://iss.moex.com/iss/engines/{engine}/markets/{market}/securities.html?iss.only=securities&marketprice_board={main_board}"
        coroutine = self.fetch_single_page(url)
        markets = self.run_fetcher(coroutine)
        if markets.empty:
            return pd.DataFrame()
        markets.columns = [i.split()[0] for i in markets.columns]
        return markets
    
    def zyc_params(self, date, show_progress=False):
        """
        Fetches zero-coupon yield curve parameters for the given date(s).
        
        Parameters:
        ----------
        date : str or list of str
            The date or list of dates to fetch yield curve parameters for.
        show_progress : bool, optional
            Flag to indicate if progress should be shown (default is False).

        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the zero-coupon yield curve parameters.
        """
        dates = [date] if isinstance(date, str) else date
        url = lambda date: f'https://iss.moex.com/iss/engines/stock/zcyc.html?iss.only=params&date={date}'
        coroutine = self.fetch_all_data(parameters=dates, url_func=url, show_progress=show_progress, pages=False)
        params = self.run_fetcher(coroutine)

        params = pd.concat(params)
        params.columns = [i.split(' ')[0] for i in params.columns]
        params.tradedate = pd.to_datetime(params.tradedate)
        return params

    def market_data(self,engine, market, isin, show_progress=False): 
        """
        Fetches market data for the given market and ISIN(s).
        
        Parameters:
        ----------
        engine : str
            The engine from ISS.
        market : str
            The market of given engine from ISS.
        isin : str or list of str
            The ISIN or list of ISINs to fetch market data for.
        show_progress : bool, optional
            Flag to indicate if progress should be shown (default is False).
            
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the market data.
        """
        self.engine_market_check(engine = engine,market = market)
        isins = [isin] if isinstance(isin, str) else isin
        url_func = lambda isin: f'https://iss.moex.com/iss/engines/{engine}/markets/{market}/securities/{isin}/history.html?iss.only=marketdata'
        coroutine = self.fetch_all_data(parameters=isins, url_func=url_func, show_progress=show_progress, pages=False)
        prices = self.run_fetcher(coroutine)
        prices = pd.concat(prices, axis=0)
        prices.columns = [i.split()[0] for i in prices.columns]
        prices['SYSTIME'] = pd.to_datetime(prices['SYSTIME'])
        
        return prices 
    
    def index_components(self, index, date, show_progress=False, pages = True): 
        """
        Fetches index components for the given index and date(s).
        
        Parameters:
        ----------
        index : str
            The index to fetch components for.
        date : str or list of str
            The date or list of dates to fetch index components for.
        show_progress : bool, optional
            Flag to indicate if progress should be shown (default is False).
            
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the index components.
        """
        dates = [date] if isinstance(date, str) else date
        url_func = lambda date: f'https://iss.moex.com/iss/statistics/engines/stock/markets/index/analytics/{index}.html?iss.only=analytics&date={date}&limit=100'
        coroutine = self.fetch_all_data(parameters=dates, url_func=url_func, show_progress=show_progress, pages=pages, records_per_page = 20)
        indx = self.run_fetcher(coroutine)
        indx = pd.concat(indx, axis=0)
        indx.columns = [i.split()[0] for i in indx.columns]
        indx = indx.drop_duplicates()
        return indx 
    
    def history_prices(self, engine,market, isin, date, show_progress=False, main_board = True):
        """
        Fetches historical prices for the given engine, ISIN, and date.
        
        Parameters:
        ----------
        engine : str
            The engine from ISS.
        market : str
            The market of given engine from ISS.
        isin : str or list of str
            The ISIN or list of ISINs to fetch historical prices for.
        date : str
            The date to fetch historical prices from.
        show_progress : bool, optional
            Flag to indicate if progress should be shown (default is False).
        main_board: bool, optiona; 
            Flag to inficate if the data contains information about main board. 
            
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the historical prices.
        """
        
        self.engine_market_check(engine = engine,market = market)
        main_board = 1 if main_board else 0 
        isins = [isin] if isinstance(isin, str) else isin
        url_func = lambda isin: f'https://iss.moex.com/iss/history/engines/{engine}/markets/{market}/securities/{isin}.html?iss.only=history&marketprice_board={main_board}&limit=100&from={date}'
        coroutine = self.fetch_all_data(parameters=isins, url_func=url_func, show_progress=show_progress, pages=True)
        indx = self.run_fetcher(coroutine)
        indx = pd.concat(indx)
        indx.columns = [i.split()[0] for i in indx.columns]
        
        return indx
    
    def candles(self, engine,market, isin, date,interval = 1, show_progress=False):
        """
        Fetches historical candels for the given engine, ISIN, and date.
        
        Parameters:
        ----------
        engine : str
            The engine from ISS.
        market : str
            The market of given engine from ISS.
        isin : str or list of str
            The ISIN or list of ISINs to fetch historical prices for.
        date : str
            The date to fetch historical prices from.
        interval : int 
            The timeframe of candel (default is 1 minute)
        show_progress : bool, optional
            Flag to indicate if progress should be shown (default is False).
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the historical prices.
        """

        self.engine_market_check(engine = engine,market = market)
        isins = [isin] if isinstance(isin, str) else isin
        url_func = lambda isin: f'https://iss.moex.com/iss/engines/{engine}/markets/{market}/securities/{isin}/candles.html?interval={interval}&from={date}'

        coroutine = self.fetch_all_data(parameters=isins, url_func=url_func, show_progress=show_progress, pages=True, records_per_page=500)   
        candles = self.run_fetcher(coroutine)
        candles = pd.concat(candles)
        candles.columns = [i.split()[0] for i in candles.columns]
        
        return candles    
    
    def trades(self, engine,market, isin, show_progress=False):
        """
        Fetches trades for the given engine, ISIN.
        
        Parameters:
        ----------
        engine : str
            The engine from ISS.
        market : str
            The market of given engine from ISS.
        isin : str or list of str
            The ISIN or list of ISINs to fetch historical prices for.
        show_progress : bool, optional
            Flag to indicate if progress should be shown (default is False).
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the historical prices.
        """

        self.engine_market_check(engine = engine,market = market)
        isins = [isin] if isinstance(isin, str) else isin
        url_func = lambda isin: f'https://iss.moex.com/iss/engines/{engine}/markets/{market}/securities/{isin}/trades.html'

        coroutine = self.fetch_all_data(parameters=isins, url_func=url_func, show_progress=show_progress, pages=True, records_per_page=500)   
        trades = self.run_fetcher(coroutine)
        trades = pd.concat(trades)
        trades.columns = [i.split()[0] for i in trades.columns]
        
        return trades 

    
    def markets(self,engine: str): 

        """
        Fetches list of markets for given engine.

        Parameters:
        ----------
        engine : str
            The engine from ISS.
        
        Returns:
        -------
        pd.DataFrame
            A DataFrame containing markets.
        """
        
        engines = [engine] if isinstance(engine, str) else engine
        url = lambda engine: f'https://iss.moex.com/iss/engines/{engine}/markets.html'
        coroutine = self.fetch_all_data(parameters=engines, url_func=url, show_progress=False, pages=False)
        markets = self.run_fetcher(coroutine)
        markets = pd.concat(markets)
        markets.columns = [i.split()[0] for i in markets.columns]

        return markets
    
    def tables_description(self,engine: str, market: str): 
        """
        Fetches description of columns in each possible table for given engine and market.

        Parameters:
        ----------
        engine : str
            The engine from ISS.
        market : str
            The market of given engine from ISS.
        
        Returns:
        -------
        dict
            Dictionary contains information about columns for each table for the market.
        """
        self.engine_market_check(engine = engine,market = market)
        tables = ['boards', 'boardgroups', 'securities', 'marketdata', 'trades', 'orderbook', 'history', 'trades_hist', 'marketdata_yields', 'trades_yields', 'history_yields', 'secstats']
        url_func = lambda table: 'https://iss.moex.com/iss/engines/{}/markets/{}.html?iss.only={}'.format(engine,market,table)



        result = {}
        for table in tables:
            url_table = url_func(table)
            coroutine = self.fetch_single_page(url_table)
            table_res = self.run_fetcher(coroutine)
            table_res.columns = [i.split()[0] for i in table_res.columns]
            result[table] = table_res

        return result 
    
    def indices(self): 
        """
        Fetches data abount indices at MOEX.

        Returns:
        -------
        pandas.DataFrame
            A DataFrame contains indices from MOEX.
        """
        url = 'https://iss.moex.com/iss/statistics/engines/stock/markets/index/analytics.html'
        coroutine = self.fetch_single_page(url)
        indecies = self.run_fetcher(coroutine)
        if indecies.empty:
            return pd.DataFrame()
        indecies.columns = [i.split()[0] for i in indecies.columns]
        return indecies
    
    def iss_url(self,url,parameters = None, pages = False, show_progress = False, records_per_pages = 20):
        """
        Fetches data from a specified URL, handling pagination if necessary.

        Parameters:
        ----------
        url : str
            The base URL to fetch data from.
        parameters : list, optional
            List of parameters to use in URL function (default is None).
        pages : bool, optional
            Whether to fetch paginated data (default is False).
        show_progress : bool, optional
            Whether to show progress (default is False).
        records_per_page: int,optional 
            The number of entries at one html page (necessary for "long" data with more entries than placed at one html page)
        Returns:
        -------
        pandas.DataFrame 
            A DataFrame contains the information from the passed url.
        """

        if type(url) == str: 
            coroutine = self.fetch_single_page(url,records_per_page = records_per_pages,pages = pages)
            df = self.run_fetcher(coroutine)
            df.columns = [i.split()[0] for i in df.columns]
            df = df.drop_duplicates(ignore_index = True)
            return df
        else: 
            if parameters is None:
                raise InvalidParametersError("Set up parameters to loop over in proper manner")
            else: 
                coroutine = self.fetch_all_data(parameters=parameters, url_func=url, show_progress=show_progress, pages=pages,records_per_page = records_per_pages)
                df_tables = self.run_fetcher(coroutine)
                df_tables = pd.concat(df_tables, axis=0)
                df_tables.columns = [i.split()[0] for i in df_tables.columns]
                return df_tables
            

    def engine_market_check(self, engine: str, market: str):
        """
        Check if the provided engine and market are valid.

        Parameters:
        ----------
        engine : str
            The engine to check.
        market : str
            The market to check.

        Raises:
        ------
        InvalidEngineError
            If the provided engine is not in the engines list.
        InvalidMarketError
            If the provided market is not valid for the given engine.
        """
        if engine not in self.engines_list:
            raise InvalidEngineError(f"Invalid engine: {engine}. Please choose a correct engine.")
        
        if market not in self.engines_markets[engine]:
            print(engine)
            print(self.engines_markets[engine])
            raise InvalidMarketError(f"Invalid market: {market} for engine: {engine}. Please choose a correct market.")
