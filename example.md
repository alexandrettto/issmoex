# Usage example of issmoex package


```python
# Installation of package
# pip install --upgrade issmoex
```


```python
# Initialization 
from issmoex import ISSMOEX
iss = ISSMOEX()
```

The structure of ISS MOEX suggests the segmentation according to engine and markets. Each engine has specific set of markets. 


```python
print('ISS engines:')
print(iss.engines)

print('\nISS engines and corresponding markets:')
print(iss.engines_markets)
```

    ISS engines:
          id           name                             title
    0      1          stock  Фондовый рынок и рынок депозитов
    1      2          state            Рынок ГЦБ (размещение)
    2      3       currency                    Валютный рынок
    3      4        futures                     Срочный рынок
    4      5      commodity                    Товарный рынок
    5      6  interventions              Товарные интервенции
    6      7       offboard                       ОТС-система
    7      9           agro                              Агро
    8   1012            otc                          ОТС с ЦК
    9   1282         quotes                             Квоты
    10  1326          money                    Денежный рынок
    
    ISS engines and corresponding markets:
    {'stock': ['index', 'shares', 'bonds', 'ndm', 'otc', 'ccp', 'deposit', 'repo', 'qnv', 'mamc', 'foreignshares', 'foreignndm', 'moexboard', 'gcc', 'credit', 'nonresndm', 'nonresrepo', 'nonresccp', 'standard', 'classica'], 'state': ['index', 'bonds', 'repo', 'ndm'], 'currency': ['otcindices', 'selt', 'futures', 'index', 'otc'], 'futures': ['main', 'forts', 'options', 'fortsiqs', 'optionsiqs'], 'commodity': ['futures'], 'interventions': ['grain'], 'offboard': ['bonds'], 'agro': ['sugar', 'auctions', 'buyauctions', 'saleauctions'], 'otc': ['shares', 'bonds', 'sharesndm', 'ndm'], 'quotes': ['bonds'], 'money': ['deposit', 'repo']}


For example, there is an interest in the assets at shares market. Hence, we choose engine = `stock` and market = `shares`. 


```python
shares_market = iss.securities_market(engine = 'stock', market = 'shares')
shares_market.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SECID</th>
      <th>BOARDID</th>
      <th>SHORTNAME</th>
      <th>PREVPRICE</th>
      <th>LOTSIZE</th>
      <th>FACEVALUE</th>
      <th>STATUS</th>
      <th>BOARDNAME</th>
      <th>DECIMALS</th>
      <th>SECNAME</th>
      <th>...</th>
      <th>PREVDATE</th>
      <th>ISSUESIZE</th>
      <th>ISIN</th>
      <th>LATNAME</th>
      <th>REGNUMBER</th>
      <th>PREVLEGALCLOSEPRICE</th>
      <th>CURRENCYID</th>
      <th>SECTYPE</th>
      <th>LISTLEVEL</th>
      <th>SETTLEDATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ABIO</td>
      <td>TQBR</td>
      <td>iАРТГЕН ао</td>
      <td>88.320</td>
      <td>10</td>
      <td>0.10</td>
      <td>A</td>
      <td>Т+: Акции и ДР - безадрес.</td>
      <td>2</td>
      <td>ПАО "Артген"</td>
      <td>...</td>
      <td>2025-01-09</td>
      <td>92645451</td>
      <td>RU000A0JNAB6</td>
      <td>ARTGEN ao</td>
      <td>1-01-08902-A</td>
      <td>89.040</td>
      <td>SUR</td>
      <td>1</td>
      <td>2</td>
      <td>2025-01-13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABRD</td>
      <td>TQBR</td>
      <td>АбрауДюрсо</td>
      <td>178.000</td>
      <td>10</td>
      <td>1.00</td>
      <td>A</td>
      <td>Т+: Акции и ДР - безадрес.</td>
      <td>1</td>
      <td>Абрау-Дюрсо ПАО ао</td>
      <td>...</td>
      <td>2025-01-09</td>
      <td>98000184</td>
      <td>RU000A0JS5T7</td>
      <td>Abrau-Durso ao</td>
      <td>1-02-12500-A</td>
      <td>178.000</td>
      <td>SUR</td>
      <td>1</td>
      <td>3</td>
      <td>2025-01-13</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ACKO</td>
      <td>TQBR</td>
      <td>АСКО ао</td>
      <td>3.580</td>
      <td>100</td>
      <td>1.00</td>
      <td>A</td>
      <td>Т+: Акции и ДР - безадрес.</td>
      <td>2</td>
      <td>АСКО ПАО ао</td>
      <td>...</td>
      <td>2025-01-09</td>
      <td>536000000</td>
      <td>RU000A0JXS91</td>
      <td>ASKO ao</td>
      <td>1-01-52065-Z</td>
      <td>3.580</td>
      <td>SUR</td>
      <td>1</td>
      <td>3</td>
      <td>2025-01-13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AFKS</td>
      <td>TQBR</td>
      <td>Система ао</td>
      <td>14.573</td>
      <td>100</td>
      <td>0.09</td>
      <td>A</td>
      <td>Т+: Акции и ДР - безадрес.</td>
      <td>3</td>
      <td>АФК "Система" ПАО ао</td>
      <td>...</td>
      <td>2025-01-09</td>
      <td>9650000000</td>
      <td>RU000A0DQZE3</td>
      <td>AFK Sistema</td>
      <td>1-05-01669-A</td>
      <td>14.606</td>
      <td>SUR</td>
      <td>1</td>
      <td>1</td>
      <td>2025-01-13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AFLT</td>
      <td>TQBR</td>
      <td>Аэрофлот</td>
      <td>58.430</td>
      <td>10</td>
      <td>1.00</td>
      <td>A</td>
      <td>Т+: Акции и ДР - безадрес.</td>
      <td>2</td>
      <td>Аэрофлот-росс.авиалин(ПАО)ао</td>
      <td>...</td>
      <td>2025-01-09</td>
      <td>3975771215</td>
      <td>RU0009062285</td>
      <td>Aeroflot</td>
      <td>1-01-00010-A</td>
      <td>58.510</td>
      <td>SUR</td>
      <td>1</td>
      <td>1</td>
      <td>2025-01-13</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>




```python
# History prices of SBER
hist_price_sber = iss.history_prices(engine = 'stock',market = 'shares',isin = 'SBER',date = '2024-01-01',show_progress=True)
hist_price_sber.head()
```

    Fetching data: 100%|██████████| 1/1 [00:00<00:00,  2.87it/s]





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BOARDID</th>
      <th>TRADEDATE</th>
      <th>SHORTNAME</th>
      <th>SECID</th>
      <th>NUMTRADES</th>
      <th>VALUE</th>
      <th>OPEN</th>
      <th>LOW</th>
      <th>HIGH</th>
      <th>LEGALCLOSEPRICE</th>
      <th>...</th>
      <th>MARKETPRICE2</th>
      <th>MARKETPRICE3</th>
      <th>ADMITTEDQUOTE</th>
      <th>MP2VALTRD</th>
      <th>MARKETPRICE3TRADESVALUE</th>
      <th>ADMITTEDVALUE</th>
      <th>WAVAL</th>
      <th>TRADINGSESSION</th>
      <th>CURRENCYID</th>
      <th>TRENDCLSPR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TQBR</td>
      <td>2024-01-03</td>
      <td>Сбербанк</td>
      <td>SBER</td>
      <td>50912</td>
      <td>5.631305e+09</td>
      <td>271.90</td>
      <td>271.00</td>
      <td>274.70</td>
      <td>273.64</td>
      <td>...</td>
      <td>273.48</td>
      <td>273.48</td>
      <td>NaN</td>
      <td>4.994800e+09</td>
      <td>4.994800e+09</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>1.38</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TQBR</td>
      <td>2024-01-04</td>
      <td>Сбербанк</td>
      <td>SBER</td>
      <td>33045</td>
      <td>3.218188e+09</td>
      <td>274.67</td>
      <td>273.70</td>
      <td>275.48</td>
      <td>274.04</td>
      <td>...</td>
      <td>274.42</td>
      <td>274.42</td>
      <td>NaN</td>
      <td>2.822724e+09</td>
      <td>2.822724e+09</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>-0.16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TQBR</td>
      <td>2024-01-05</td>
      <td>Сбербанк</td>
      <td>SBER</td>
      <td>26234</td>
      <td>2.634960e+09</td>
      <td>274.30</td>
      <td>272.80</td>
      <td>274.69</td>
      <td>273.46</td>
      <td>...</td>
      <td>273.46</td>
      <td>273.46</td>
      <td>NaN</td>
      <td>2.246293e+09</td>
      <td>2.246293e+09</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>-0.18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TQBR</td>
      <td>2024-01-08</td>
      <td>Сбербанк</td>
      <td>SBER</td>
      <td>70828</td>
      <td>5.924626e+09</td>
      <td>273.60</td>
      <td>273.53</td>
      <td>277.00</td>
      <td>275.81</td>
      <td>...</td>
      <td>275.61</td>
      <td>275.61</td>
      <td>NaN</td>
      <td>5.204970e+09</td>
      <td>5.204970e+09</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>1.15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TQBR</td>
      <td>2024-01-09</td>
      <td>Сбербанк</td>
      <td>SBER</td>
      <td>40508</td>
      <td>5.601231e+09</td>
      <td>276.97</td>
      <td>274.71</td>
      <td>278.00</td>
      <td>276.00</td>
      <td>...</td>
      <td>275.71</td>
      <td>275.71</td>
      <td>NaN</td>
      <td>4.962470e+09</td>
      <td>4.962470e+09</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>-0.53</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>



Suppose there is a necessity to load the history prices for several shares: SBER, GAZP and AFKS. 


```python
isins = ['SBER','GAZP','AFKS']
hist_prices = iss.history_prices(engine = 'stock',market = 'shares',isin = isins,date = '2024-01-01',show_progress=True)
hist_prices.head()
```

    Fetching data: 100%|██████████| 3/3 [00:00<00:00,  6.68it/s]





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BOARDID</th>
      <th>TRADEDATE</th>
      <th>SHORTNAME</th>
      <th>SECID</th>
      <th>NUMTRADES</th>
      <th>VALUE</th>
      <th>OPEN</th>
      <th>LOW</th>
      <th>HIGH</th>
      <th>LEGALCLOSEPRICE</th>
      <th>...</th>
      <th>MARKETPRICE2</th>
      <th>MARKETPRICE3</th>
      <th>ADMITTEDQUOTE</th>
      <th>MP2VALTRD</th>
      <th>MARKETPRICE3TRADESVALUE</th>
      <th>ADMITTEDVALUE</th>
      <th>WAVAL</th>
      <th>TRADINGSESSION</th>
      <th>CURRENCYID</th>
      <th>TRENDCLSPR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TQBR</td>
      <td>2024-01-03</td>
      <td>Система ао</td>
      <td>AFKS</td>
      <td>5726</td>
      <td>157654982.7</td>
      <td>16.242</td>
      <td>16.240</td>
      <td>16.439</td>
      <td>16.287</td>
      <td>...</td>
      <td>16.350</td>
      <td>16.350</td>
      <td>NaN</td>
      <td>120895648.7</td>
      <td>120895648.7</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>-0.07</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TQBR</td>
      <td>2024-01-04</td>
      <td>Система ао</td>
      <td>AFKS</td>
      <td>7088</td>
      <td>216106558.3</td>
      <td>16.330</td>
      <td>16.200</td>
      <td>16.425</td>
      <td>16.367</td>
      <td>...</td>
      <td>16.308</td>
      <td>16.308</td>
      <td>NaN</td>
      <td>157139268.8</td>
      <td>157139268.8</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>0.53</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TQBR</td>
      <td>2024-01-05</td>
      <td>Система ао</td>
      <td>AFKS</td>
      <td>6364</td>
      <td>141240521.8</td>
      <td>16.420</td>
      <td>16.261</td>
      <td>16.494</td>
      <td>16.300</td>
      <td>...</td>
      <td>16.388</td>
      <td>16.388</td>
      <td>NaN</td>
      <td>97922427.8</td>
      <td>97922427.8</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>-0.63</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TQBR</td>
      <td>2024-01-08</td>
      <td>Система ао</td>
      <td>AFKS</td>
      <td>9489</td>
      <td>256345397.4</td>
      <td>16.300</td>
      <td>16.300</td>
      <td>16.594</td>
      <td>16.594</td>
      <td>...</td>
      <td>16.511</td>
      <td>16.511</td>
      <td>NaN</td>
      <td>227714938.0</td>
      <td>227714938.0</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>1.65</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TQBR</td>
      <td>2024-01-09</td>
      <td>Система ао</td>
      <td>AFKS</td>
      <td>10138</td>
      <td>274169410.3</td>
      <td>16.512</td>
      <td>16.439</td>
      <td>16.592</td>
      <td>16.486</td>
      <td>...</td>
      <td>16.511</td>
      <td>16.511</td>
      <td>NaN</td>
      <td>209621139.0</td>
      <td>209621139.0</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>SUR</td>
      <td>-0.44</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>



Also ISS provides the information about best offer and best bid with time lag of 15 minutes for different boards


```python
iss.market_data(engine = 'stock',market = 'shares',isin = 'SBER')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SECID</th>
      <th>BOARDID</th>
      <th>BID</th>
      <th>BIDDEPTH</th>
      <th>OFFER</th>
      <th>OFFERDEPTH</th>
      <th>SPREAD</th>
      <th>BIDDEPTHT</th>
      <th>OFFERDEPTHT</th>
      <th>OPEN</th>
      <th>...</th>
      <th>SEQNUM</th>
      <th>SYSTIME</th>
      <th>CLOSINGAUCTIONPRICE</th>
      <th>CLOSINGAUCTIONVOLUME</th>
      <th>ISSUECAPITALIZATION</th>
      <th>ISSUECAPITALIZATION_UPDATETIME</th>
      <th>ETFSETTLECURRENCY</th>
      <th>VALTODAY_RUR</th>
      <th>TRADINGSESSION</th>
      <th>TRENDISSUECAPITALIZATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SBER</td>
      <td>SMAL</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>273.97</td>
      <td>...</td>
      <td>20250111000501</td>
      <td>2025-01-11 00:05:01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6017793493960</td>
      <td>23:49:57</td>
      <td>NaN</td>
      <td>748730</td>
      <td>NaN</td>
      <td>150461027560</td>
    </tr>
    <tr>
      <th>1</th>
      <td>SBER</td>
      <td>SPEQ</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>...</td>
      <td>20250111000501</td>
      <td>2025-01-11 00:05:01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6017793493960</td>
      <td>23:49:57</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>150461027560</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SBER</td>
      <td>TQBR</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>272.31</td>
      <td>...</td>
      <td>20250111000501</td>
      <td>2025-01-11 00:05:01</td>
      <td>278.17</td>
      <td>50660.0</td>
      <td>6017793493960</td>
      <td>23:49:57</td>
      <td>NaN</td>
      <td>19623132401</td>
      <td>NaN</td>
      <td>150461027560</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 56 columns</p>
</div>



Now, it's unclear what is `BIDDEPTHT` feature. The function - `tables_description` can help to get description for every table


```python
descriptions = iss.tables_description(engine = 'stock', market = 'shares')
marketdata_desc = descriptions['marketdata']
marketdata_desc.head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>short_title</th>
      <th>title</th>
      <th>is_ordered</th>
      <th>is_system</th>
      <th>is_hidden</th>
      <th>trend_by</th>
      <th>is_signed</th>
      <th>has_percent</th>
      <th>type</th>
      <th>precision</th>
      <th>is_linked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1866</td>
      <td>SECID</td>
      <td>Код инструмента</td>
      <td>Идентификатор финансового инструмента</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>string</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1865</td>
      <td>BOARDID</td>
      <td>Код режима</td>
      <td>Идентификатор режима торгов</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>string</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1868</td>
      <td>BID</td>
      <td>Спрос</td>
      <td>Лучшая котировка на покупку</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1869</td>
      <td>BIDDEPTH</td>
      <td>Лотов на покупку по лучшей</td>
      <td>Объем заявок на покупку по лучшей котировке, в...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1872</td>
      <td>OFFER</td>
      <td>Предложение</td>
      <td>Лучшая котировка на продажу</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1873</td>
      <td>OFFERDEPTH</td>
      <td>Лотов на продажу по лучшей</td>
      <td>Объем заявок на продажу по лучшей котировке, в...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1914</td>
      <td>SPREAD</td>
      <td>Спред</td>
      <td>Разница между лучшей котировкой на продажу и п...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1870</td>
      <td>BIDDEPTHT</td>
      <td>Совокупный спрос</td>
      <td>Объем всех заявок на покупку в очереди Торгово...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1874</td>
      <td>OFFERDEPTHT</td>
      <td>Совокупное предложение</td>
      <td>Объем всех заявок на продажу в очереди Торгово...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1876</td>
      <td>OPEN</td>
      <td>Первая</td>
      <td>Цена первой сделки</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1878</td>
      <td>LOW</td>
      <td>Минимум</td>
      <td>Минимальная цена сделки</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1877</td>
      <td>HIGH</td>
      <td>Максимум</td>
      <td>Максимальная цена сделки</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1879</td>
      <td>LAST</td>
      <td>Последняя</td>
      <td>Цена последней сделки</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1915.0</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1913</td>
      <td>LASTCHANGE</td>
      <td>Изменение последней, руб.</td>
      <td>Изменение цены последней сделки к цене предыду...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1913.0</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1881</td>
      <td>LASTCHANGEPRCNT</td>
      <td>Изменение последней, %</td>
      <td>Изменение цены последней сделки к цене предыду...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1881.0</td>
      <td>1</td>
      <td>1</td>
      <td>number</td>
      <td>2.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1884</td>
      <td>QTY</td>
      <td>Лотов в последней</td>
      <td>Объем последней сделки, в лотах</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1890</td>
      <td>VALUE</td>
      <td>Объем в последней</td>
      <td>Объем последней сделки, в руб.</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1891</td>
      <td>VALUE_USD</td>
      <td>Объем последней, дол. США</td>
      <td>Объем последней сделки, дол. США</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>2.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1892</td>
      <td>WAPRICE</td>
      <td>Ср.взвеш.</td>
      <td>Средневзвешенная цена</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1893.0</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1883</td>
      <td>LASTCNGTOLASTWAPRICE</td>
      <td>Изменение к средневзвешенной цене</td>
      <td>Изменение цены последней сделки к средневзвеше...</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1883.0</td>
      <td>0</td>
      <td>0</td>
      <td>number</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



Also ISS provides an information about candels for different instruments. 



```python
# 1-minute candels for SBER from 2024-11-20
candles = iss.candles('stock','shares','SBER','2024-11-20',show_progress=False)
candles.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>value</th>
      <th>volume</th>
      <th>begin</th>
      <th>end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>241.82</td>
      <td>241.82</td>
      <td>241.82</td>
      <td>241.82</td>
      <td>27286968.8</td>
      <td>112840</td>
      <td>2024-11-20 09:59:00</td>
      <td>2024-11-20 09:59:59</td>
    </tr>
    <tr>
      <th>1</th>
      <td>241.80</td>
      <td>241.89</td>
      <td>242.28</td>
      <td>241.55</td>
      <td>166152508.1</td>
      <td>686900</td>
      <td>2024-11-20 10:00:00</td>
      <td>2024-11-20 10:00:59</td>
    </tr>
    <tr>
      <th>2</th>
      <td>241.81</td>
      <td>241.73</td>
      <td>242.19</td>
      <td>241.67</td>
      <td>123881188.3</td>
      <td>512060</td>
      <td>2024-11-20 10:01:00</td>
      <td>2024-11-20 10:01:59</td>
    </tr>
    <tr>
      <th>3</th>
      <td>241.72</td>
      <td>242.03</td>
      <td>242.08</td>
      <td>241.60</td>
      <td>64168699.3</td>
      <td>265340</td>
      <td>2024-11-20 10:02:00</td>
      <td>2024-11-20 10:02:59</td>
    </tr>
    <tr>
      <th>4</th>
      <td>242.04</td>
      <td>241.89</td>
      <td>242.28</td>
      <td>241.72</td>
      <td>79630783.9</td>
      <td>329050</td>
      <td>2024-11-20 10:03:00</td>
      <td>2024-11-20 10:03:59</td>
    </tr>
  </tbody>
</table>
</div>



ISS also provides information about different indecies at MOEX and their components. 


```python
indices = iss.indices()
indices.head()

index = 'IMOEX'
IMOEX = iss.index_components(index = index, date = '2024-06-11')
IMOEX.head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>indexid</th>
      <th>tradedate</th>
      <th>ticker</th>
      <th>shortnames</th>
      <th>secids</th>
      <th>weight</th>
      <th>tradingsession</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>AFKS</td>
      <td>Система ао</td>
      <td>AFKS</td>
      <td>0.89</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>AFLT</td>
      <td>Аэрофлот</td>
      <td>AFLT</td>
      <td>0.83</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>AGRO</td>
      <td>AGRO-гдр</td>
      <td>AGRO</td>
      <td>0.86</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>ALRS</td>
      <td>АЛРОСА ао</td>
      <td>ALRS</td>
      <td>1.34</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>BSPB</td>
      <td>БСП ао</td>
      <td>BSPB</td>
      <td>0.45</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>CBOM</td>
      <td>МКБ ао</td>
      <td>CBOM</td>
      <td>0.63</td>
      <td>3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>CHMF</td>
      <td>СевСт-ао</td>
      <td>CHMF</td>
      <td>2.51</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>ENPG</td>
      <td>ЭН+ГРУП ао</td>
      <td>ENPG</td>
      <td>0.43</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>FEES</td>
      <td>Россети</td>
      <td>FEES</td>
      <td>0.42</td>
      <td>3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>FIVE</td>
      <td>FIVE-гдр</td>
      <td>FIVE</td>
      <td>1.11</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>FLOT</td>
      <td>Совкомфлот</td>
      <td>FLOT</td>
      <td>0.60</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>GAZP</td>
      <td>ГАЗПРОМ ао</td>
      <td>GAZP</td>
      <td>8.67</td>
      <td>3</td>
    </tr>
    <tr>
      <th>12</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>GLTR</td>
      <td>GLTR-гдр</td>
      <td>GLTR</td>
      <td>0.25</td>
      <td>3</td>
    </tr>
    <tr>
      <th>13</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>GMKN</td>
      <td>ГМКНорНик</td>
      <td>GMKN</td>
      <td>6.10</td>
      <td>3</td>
    </tr>
    <tr>
      <th>14</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>HYDR</td>
      <td>РусГидро</td>
      <td>HYDR</td>
      <td>0.23</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>IRAO</td>
      <td>ИнтерРАОао</td>
      <td>IRAO</td>
      <td>1.51</td>
      <td>3</td>
    </tr>
    <tr>
      <th>16</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>LKOH</td>
      <td>ЛУКОЙЛ</td>
      <td>LKOH</td>
      <td>15.19</td>
      <td>3</td>
    </tr>
    <tr>
      <th>17</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>MAGN</td>
      <td>ММК</td>
      <td>MAGN</td>
      <td>1.32</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>MGNT</td>
      <td>Магнит ао</td>
      <td>MGNT</td>
      <td>1.31</td>
      <td>3</td>
    </tr>
    <tr>
      <th>19</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>MOEX</td>
      <td>МосБиржа</td>
      <td>MOEX</td>
      <td>1.33</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



Also, ISS MOEX provides the time schedule of bonds' coupons and amortization payments. Let's conisder based on following example: 


```python
bonds_market = iss.securities_market(engine = 'stock', market = 'bonds')
bonds_market.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SECID</th>
      <th>BOARDID</th>
      <th>SHORTNAME</th>
      <th>PREVWAPRICE</th>
      <th>YIELDATPREVWAPRICE</th>
      <th>COUPONVALUE</th>
      <th>NEXTCOUPON</th>
      <th>ACCRUEDINT</th>
      <th>PREVPRICE</th>
      <th>LOTSIZE</th>
      <th>...</th>
      <th>REGNUMBER</th>
      <th>CURRENCYID</th>
      <th>ISSUESIZEPLACED</th>
      <th>LISTLEVEL</th>
      <th>SECTYPE</th>
      <th>COUPONPERCENT</th>
      <th>OFFERDATE</th>
      <th>SETTLEDATE</th>
      <th>LOTVALUE</th>
      <th>FACEVALUEONSETTLEDATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KG000A3LSC78</td>
      <td>TQCB</td>
      <td>Кыргыз. 01</td>
      <td>98.999</td>
      <td>16.99</td>
      <td>3.88</td>
      <td>2024-06-25</td>
      <td>3.434903</td>
      <td>98.999</td>
      <td>1</td>
      <td>...</td>
      <td>NaN</td>
      <td>SUR</td>
      <td>NaN</td>
      <td>3</td>
      <td>6</td>
      <td>15.50</td>
      <td>NaN</td>
      <td>2024-06-13</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>KG000A3LSJ06</td>
      <td>TQCB</td>
      <td>Кыргыз. 02</td>
      <td>97.410</td>
      <td>17.20</td>
      <td>3.63</td>
      <td>2024-06-26</td>
      <td>3.101389</td>
      <td>97.050</td>
      <td>1</td>
      <td>...</td>
      <td>NaN</td>
      <td>SUR</td>
      <td>NaN</td>
      <td>3</td>
      <td>6</td>
      <td>14.50</td>
      <td>NaN</td>
      <td>2024-06-13</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RU000A0JQ7Z2</td>
      <td>TQCB</td>
      <td>РЖД-19 обл</td>
      <td>99.830</td>
      <td>10.29</td>
      <td>39.14</td>
      <td>2024-07-08</td>
      <td>33.770000</td>
      <td>99.860</td>
      <td>1</td>
      <td>...</td>
      <td>4-19-65045-D</td>
      <td>SUR</td>
      <td>10000000.0</td>
      <td>2</td>
      <td>6</td>
      <td>7.85</td>
      <td>NaN</td>
      <td>2024-06-13</td>
      <td>1000.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RU000A0JQAM6</td>
      <td>TQCB</td>
      <td>ДОМ.РФ15об</td>
      <td>106.800</td>
      <td>-5.58</td>
      <td>93.26</td>
      <td>2024-09-15</td>
      <td>45.620000</td>
      <td>106.800</td>
      <td>1</td>
      <td>...</td>
      <td>4-15-00739-A</td>
      <td>SUR</td>
      <td>7000000.0</td>
      <td>1</td>
      <td>6</td>
      <td>18.50</td>
      <td>NaN</td>
      <td>2024-06-13</td>
      <td>1000.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>RU000A0JQRD9</td>
      <td>TQCB</td>
      <td>РЖД-23 обл</td>
      <td>95.530</td>
      <td>16.54</td>
      <td>39.14</td>
      <td>2024-07-18</td>
      <td>31.620000</td>
      <td>96.050</td>
      <td>1</td>
      <td>...</td>
      <td>4-23-65045-D</td>
      <td>SUR</td>
      <td>15000000.0</td>
      <td>2</td>
      <td>6</td>
      <td>7.85</td>
      <td>NaN</td>
      <td>2024-06-13</td>
      <td>1000.0</td>
      <td>1000.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 40 columns</p>
</div>




```python
bonds_market.columns
```




    Index(['SECID', 'BOARDID', 'SHORTNAME', 'PREVWAPRICE', 'YIELDATPREVWAPRICE',
           'COUPONVALUE', 'NEXTCOUPON', 'ACCRUEDINT', 'PREVPRICE', 'LOTSIZE',
           'FACEVALUE', 'BOARDNAME', 'STATUS', 'MATDATE', 'DECIMALS',
           'COUPONPERIOD', 'ISSUESIZE', 'PREVLEGALCLOSEPRICE', 'PREVDATE',
           'SECNAME', 'REMARKS', 'MARKETCODE', 'INSTRID', 'SECTORID', 'MINSTEP',
           'FACEUNIT', 'BUYBACKPRICE', 'BUYBACKDATE', 'ISIN', 'LATNAME',
           'REGNUMBER', 'CURRENCYID', 'ISSUESIZEPLACED', 'LISTLEVEL', 'SECTYPE',
           'COUPONPERCENT', 'OFFERDATE', 'SETTLEDATE', 'LOTVALUE',
           'FACEVALUEONSETTLEDATE'],
          dtype='object')




```python
url = 'https://iss.moex.com/iss/apps/infogrid/emission/rates.csv?iss.dp=comma&iss.df=%25d.%25m.%25Y&iss.tf=%25H:%25M:%25S&iss.dtf=%25d.%25m.%25Y%20%25H:%25M:%25S&iss.only=rates&limit=unlimited&lang=ru'
market_full = pd.read_csv(url, skiprows=1, delimiter=';', encoding='windows-1251') # Get all tradable bonds
market_full['INN']
```


```python

```




    0           5403
    1          97053
    2           3850
    3           3850
    4           3850
              ...   
    3185    10035220
    3186    10035220
    3187    10035220
    3188    10035220
    3189    10035220
    Name: INN, Length: 3190, dtype: int64




```python
isins = bonds_market['SECID'].iloc[:20].to_list()
bonds_coupons = iss.bonds_coupons(isin = isins)
bonds_amort = iss.bonds_amort(isin = isins)
```

    Fetching data: 100%|████████████████████████████| 20/20 [00:01<00:00, 15.98it/s]
    Fetching data: 100%|████████████████████████████| 20/20 [00:03<00:00,  6.17it/s]



```python
bonds_coupons.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>isin</th>
      <th>name</th>
      <th>issuevalue</th>
      <th>coupondate</th>
      <th>recorddate</th>
      <th>startdate</th>
      <th>initialfacevalue</th>
      <th>facevalue</th>
      <th>faceunit</th>
      <th>value</th>
      <th>valueprc</th>
      <th>value_rub</th>
      <th>secid</th>
      <th>primary_boardid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RU000A0JS4Z7</td>
      <td>ВЭБ.РФ об. сер. 21</td>
      <td>15000000000</td>
      <td>2012-09-11</td>
      <td>NaT</td>
      <td>2012-03-13</td>
      <td>1000</td>
      <td>1000</td>
      <td>RUB</td>
      <td>41.88</td>
      <td>8.4</td>
      <td>41.88</td>
      <td>RU000A0JS4Z7</td>
      <td>TQCB</td>
    </tr>
    <tr>
      <th>1</th>
      <td>RU000A0JS4Z7</td>
      <td>ВЭБ.РФ об. сер. 21</td>
      <td>15000000000</td>
      <td>2013-03-12</td>
      <td>NaT</td>
      <td>2012-09-11</td>
      <td>1000</td>
      <td>1000</td>
      <td>RUB</td>
      <td>41.88</td>
      <td>8.4</td>
      <td>41.88</td>
      <td>RU000A0JS4Z7</td>
      <td>TQCB</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RU000A0JS4Z7</td>
      <td>ВЭБ.РФ об. сер. 21</td>
      <td>15000000000</td>
      <td>2013-09-10</td>
      <td>NaT</td>
      <td>2013-03-12</td>
      <td>1000</td>
      <td>1000</td>
      <td>RUB</td>
      <td>41.88</td>
      <td>8.4</td>
      <td>41.88</td>
      <td>RU000A0JS4Z7</td>
      <td>TQCB</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RU000A0JS4Z7</td>
      <td>ВЭБ.РФ об. сер. 21</td>
      <td>15000000000</td>
      <td>2014-03-11</td>
      <td>NaT</td>
      <td>2013-09-10</td>
      <td>1000</td>
      <td>1000</td>
      <td>RUB</td>
      <td>41.88</td>
      <td>8.4</td>
      <td>41.88</td>
      <td>RU000A0JS4Z7</td>
      <td>TQCB</td>
    </tr>
    <tr>
      <th>4</th>
      <td>RU000A0JS4Z7</td>
      <td>ВЭБ.РФ об. сер. 21</td>
      <td>15000000000</td>
      <td>2014-09-09</td>
      <td>NaT</td>
      <td>2014-03-11</td>
      <td>1000</td>
      <td>1000</td>
      <td>RUB</td>
      <td>41.88</td>
      <td>8.4</td>
      <td>41.88</td>
      <td>RU000A0JS4Z7</td>
      <td>TQCB</td>
    </tr>
  </tbody>
</table>
</div>




```python
bonds_amort.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>isin</th>
      <th>name</th>
      <th>issuevalue</th>
      <th>amortdate</th>
      <th>facevalue</th>
      <th>initialfacevalue</th>
      <th>faceunit</th>
      <th>valueprc</th>
      <th>value</th>
      <th>value_rub</th>
      <th>data_source</th>
      <th>secid</th>
      <th>primary_boardid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KG000A3LSJ06</td>
      <td>Республика Кыргызстан 02</td>
      <td>1000000000</td>
      <td>2025-12-26</td>
      <td>100</td>
      <td>100</td>
      <td>RUB</td>
      <td>100.0</td>
      <td>100</td>
      <td>100.00</td>
      <td>maturity</td>
      <td>KG000A3LSJ06</td>
      <td>TQCB</td>
    </tr>
    <tr>
      <th>0</th>
      <td>RU000A0JQAM6</td>
      <td>ДОМ.РФ (АО) обл. сер. А15</td>
      <td>7000000000</td>
      <td>2028-09-15</td>
      <td>1000</td>
      <td>1000</td>
      <td>RUB</td>
      <td>100.0</td>
      <td>1000</td>
      <td>1000.00</td>
      <td>maturity</td>
      <td>RU000A0JQAM6</td>
      <td>TQCB</td>
    </tr>
    <tr>
      <th>0</th>
      <td>RU000A0JRZ74</td>
      <td>ПАО ОТКРЫТИЕ ФК Банк БО-03</td>
      <td>18000000000</td>
      <td>2025-07-16</td>
      <td>1000</td>
      <td>1000</td>
      <td>RUB</td>
      <td>100.0</td>
      <td>1000</td>
      <td>1000.00</td>
      <td>maturity</td>
      <td>RU000A0JRZ74</td>
      <td>TQCB</td>
    </tr>
    <tr>
      <th>0</th>
      <td>RU000A0JS4J1</td>
      <td>Запад.скор.диаметр АО об.03</td>
      <td>5000000000</td>
      <td>2032-02-06</td>
      <td>1000</td>
      <td>1000</td>
      <td>RUB</td>
      <td>100.0</td>
      <td>1000</td>
      <td>1000.00</td>
      <td>maturity</td>
      <td>RU000A0JS4J1</td>
      <td>TQCB</td>
    </tr>
    <tr>
      <th>0</th>
      <td>KG000A3LSC78</td>
      <td>Республика Кыргызстан 01</td>
      <td>1000000000</td>
      <td>2025-12-25</td>
      <td>100</td>
      <td>100</td>
      <td>KGS</td>
      <td>100.0</td>
      <td>100</td>
      <td>102.33</td>
      <td>maturity</td>
      <td>KG000A3LSC78</td>
      <td>TQCB</td>
    </tr>
  </tbody>
</table>
</div>



The package provides an opportunity to operate with custom urls from ISS. 


```python
# Accrued interest on the end of month
# Single page version without 
url = 'https://iss.moex.com/iss/statistics/engines/stock/markets/bonds/monthendaccints.html'
iss.iss_url(url)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tradedate</th>
      <th>secid</th>
      <th>name</th>
      <th>shortname</th>
      <th>regnumber</th>
      <th>accint</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-03-31</td>
      <td>AT0000A2UF10</td>
      <td>Raiffeisen Bank Int AG</td>
      <td>Raiff BIAG</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-03-31</td>
      <td>CH0248531110</td>
      <td>VTB CAPITAL S.A. 24 CHF</td>
      <td>VTB-24 CHF</td>
      <td>NaN</td>
      <td>88.803125</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-03-31</td>
      <td>CH0419041618</td>
      <td>RZD CAPITAL PLC 0.898 03/10/25</td>
      <td>RZD-25 CHF</td>
      <td>NaN</td>
      <td>22.200556</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-03-31</td>
      <td>CH0419041634</td>
      <td>RZD CAPITAL PLC 03/04/28</td>
      <td>RZD-28 CHF</td>
      <td>NaN</td>
      <td>59.418056</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-03-31</td>
      <td>CH1100259816</td>
      <td>RZD Capital PLC VAR UNDT</td>
      <td>RZD-p CHF</td>
      <td>NaN</td>
      <td>120.225694</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3033</th>
      <td>2024-03-31</td>
      <td>XS2420560869</td>
      <td>BCS SP Plc Series 239</td>
      <td>BCS01/25</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3034</th>
      <td>2024-03-31</td>
      <td>XS2423361190</td>
      <td>BCS SP Plc Series 240</td>
      <td>BCS02/27-4</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3035</th>
      <td>2024-03-31</td>
      <td>XS2429208486</td>
      <td>BCS SP Plc Series 243</td>
      <td>BCS05/25</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3036</th>
      <td>2024-03-31</td>
      <td>XS2439218640</td>
      <td>BCS SP Plc Series 244</td>
      <td>BCS06/25-B</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3037</th>
      <td>2024-03-31</td>
      <td>XS2446844321</td>
      <td>BCS SP Plc Series 245</td>
      <td>BCS06/25-C</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>3038 rows × 6 columns</p>
</div>




```python
# Market Data of Yields
# Example of custom url function iterable over defined number of parameters
url_func = lambda isin: f'https://iss.moex.com/iss/engines/stock/markets/bonds/securities/{isin}.html?iss.only=marketdata_yields'
bonds_market_yields = iss.iss_url(url = url_func, parameters = isins)
bonds_market_yields.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SECID</th>
      <th>BOARDID</th>
      <th>PRICE</th>
      <th>YIELDDATE</th>
      <th>ZCYCMOMENT</th>
      <th>YIELDDATETYPE</th>
      <th>EFFECTIVEYIELD</th>
      <th>DURATION</th>
      <th>ZSPREADBP</th>
      <th>GSPREADBP</th>
      <th>...</th>
      <th>DURATIONWAPRICE</th>
      <th>IR</th>
      <th>ICPI</th>
      <th>BEI</th>
      <th>CBR</th>
      <th>YIELDTOOFFER</th>
      <th>YIELDLASTCOUPON</th>
      <th>TRADEMOMENT</th>
      <th>SEQNUM</th>
      <th>SYSTIME</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RU000A0JS4K9</td>
      <td>TQCB</td>
      <td>105.99</td>
      <td>2032-02-06</td>
      <td>2024-06-11 16:36:06</td>
      <td>MATDATE</td>
      <td>8.9387</td>
      <td>1992</td>
      <td>-618</td>
      <td>-629</td>
      <td>...</td>
      <td>1992.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2024-06-11 16:36:37</td>
      <td>20240611165100</td>
      <td>2024-06-11 16:51:00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>RU000A0JS4Z7</td>
      <td>TQCB</td>
      <td>95.20</td>
      <td>2032-02-17</td>
      <td>2024-06-11 14:16:51</td>
      <td>MATDATE</td>
      <td>10.4502</td>
      <td>1989</td>
      <td>-463</td>
      <td>-471</td>
      <td>...</td>
      <td>1990.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2024-06-11 14:16:52</td>
      <td>20240611143100</td>
      <td>2024-06-11 14:31:00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>RU000A0JS4L7</td>
      <td>TQCB</td>
      <td>116.30</td>
      <td>2032-02-06</td>
      <td>2024-06-10 18:39:59</td>
      <td>MATDATE</td>
      <td>7.1708</td>
      <td>2033</td>
      <td>-794</td>
      <td>-804</td>
      <td>...</td>
      <td>2033.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2024-06-06 23:59:59</td>
      <td>20240611062613</td>
      <td>2024-06-11 06:26:13</td>
    </tr>
    <tr>
      <th>0</th>
      <td>KG000A3LSC78</td>
      <td>TQCB</td>
      <td>99.00</td>
      <td>2025-12-25</td>
      <td>2024-06-11 10:17:53</td>
      <td>MATDATE</td>
      <td>16.9939</td>
      <td>492</td>
      <td>106</td>
      <td>105</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2024-06-11 10:17:57</td>
      <td>20240611103200</td>
      <td>2024-06-11 10:32:00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>RU000A0JSQ58</td>
      <td>TQCB</td>
      <td>99.99</td>
      <td>2024-07-31</td>
      <td>2024-06-11 11:39:58</td>
      <td>OFFER</td>
      <td>7.9261</td>
      <td>47</td>
      <td>-702</td>
      <td>-702</td>
      <td>...</td>
      <td>47.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.9261</td>
      <td>NaN</td>
      <td>2024-06-11 11:47:30</td>
      <td>20240611120200</td>
      <td>2024-06-11 12:02:00</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>




```python
date = '2024-01-01'
url_func = lambda isin: f'https://iss.moex.com/iss/history/engines/stock/markets/bonds/yields/{isin}.html?from={date}&limit=100'
bonds_market_yields_history = iss.iss_url(url = url_func, 
                                          parameters = isins,
                                          pages = True, #to iterate over all page entries
                                          show_progress = True, 
                                          records_per_pages = 100 )#depicted number of rows at one iteration)
bonds_market_yields_history.head()

```

    Fetching data: 100%|████████████████████████████| 20/20 [00:01<00:00, 14.39it/s]





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TRADEDATE</th>
      <th>SECID</th>
      <th>BOARDID</th>
      <th>YIELDDATE</th>
      <th>YIELDDATETYPE</th>
      <th>PRICE</th>
      <th>ACCINT</th>
      <th>ZCYCMOMENT</th>
      <th>EFFECTIVEYIELD</th>
      <th>DURATION</th>
      <th>...</th>
      <th>WAPRICE</th>
      <th>EFFECTIVEYIELDWAPRICE</th>
      <th>DURATIONWAPRICE</th>
      <th>IR</th>
      <th>ICPI</th>
      <th>BEI</th>
      <th>CBR</th>
      <th>YIELDTOOFFER</th>
      <th>YIELDLASTCOUPON</th>
      <th>TRADEMOMENT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-03</td>
      <td>RU000A0JRZ74</td>
      <td>TQCB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-04</td>
      <td>RU000A0JRZ74</td>
      <td>TQCB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-05</td>
      <td>RU000A0JRZ74</td>
      <td>TQCB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-08</td>
      <td>RU000A0JRZ74</td>
      <td>TQCB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-09</td>
      <td>RU000A0JRZ74</td>
      <td>TQCB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



The package has docstring description. For conveince use the following query to get information about function and
variables


```python
?iss.iss_url
```

### Advantages of package

The package has several advantages: 

1. Simplifies work with ISS MOEX, as most frequent queries are defined in the easy reading functions 
2. Signficantly speed up the urls requests, because of asynchronous framework usage 
3. Allows to work with custom ISS requests, accounting for all specificity of the requests


### Time difference with usual requests 

The comparision will be done with `pd.read_html()` method, which is the easiest method to interact with html tables. 

The design of experiment will be following: 

1. 20 stocks from IMOEX 
2. History prices from 2023-01-01



```python
IMOEX.sort_values(by = 'weight',ascending = False, inplace = True)
stocks = IMOEX['secids'].iloc[:20].to_list()
IMOEX.head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>indexid</th>
      <th>tradedate</th>
      <th>ticker</th>
      <th>shortnames</th>
      <th>secids</th>
      <th>weight</th>
      <th>tradingsession</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>LKOH</td>
      <td>ЛУКОЙЛ</td>
      <td>LKOH</td>
      <td>15.19</td>
      <td>3</td>
    </tr>
    <tr>
      <th>34</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>SBER</td>
      <td>Сбербанк</td>
      <td>SBER</td>
      <td>14.05</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>GAZP</td>
      <td>ГАЗПРОМ ао</td>
      <td>GAZP</td>
      <td>8.67</td>
      <td>3</td>
    </tr>
    <tr>
      <th>13</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>GMKN</td>
      <td>ГМКНорНик</td>
      <td>GMKN</td>
      <td>6.10</td>
      <td>3</td>
    </tr>
    <tr>
      <th>41</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>TATN</td>
      <td>Татнфт 3ао</td>
      <td>TATN</td>
      <td>6.00</td>
      <td>3</td>
    </tr>
    <tr>
      <th>25</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>NVTK</td>
      <td>Новатэк ао</td>
      <td>NVTK</td>
      <td>3.65</td>
      <td>3</td>
    </tr>
    <tr>
      <th>40</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>SNGSP</td>
      <td>Сургнфгз-п</td>
      <td>SNGSP</td>
      <td>3.43</td>
      <td>3</td>
    </tr>
    <tr>
      <th>39</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>SNGS</td>
      <td>Сургнфгз</td>
      <td>SNGS</td>
      <td>3.21</td>
      <td>3</td>
    </tr>
    <tr>
      <th>35</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>SBERP</td>
      <td>Сбербанк-п</td>
      <td>SBERP</td>
      <td>2.71</td>
      <td>3</td>
    </tr>
    <tr>
      <th>29</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>PLZL</td>
      <td>Полюс</td>
      <td>PLZL</td>
      <td>2.60</td>
      <td>3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>CHMF</td>
      <td>СевСт-ао</td>
      <td>CHMF</td>
      <td>2.51</td>
      <td>3</td>
    </tr>
    <tr>
      <th>31</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>ROSN</td>
      <td>Роснефть</td>
      <td>ROSN</td>
      <td>2.34</td>
      <td>3</td>
    </tr>
    <tr>
      <th>28</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>PIKK</td>
      <td>ПИК ао</td>
      <td>PIKK</td>
      <td>1.84</td>
      <td>3</td>
    </tr>
    <tr>
      <th>24</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>NLMK</td>
      <td>НЛМК ао</td>
      <td>NLMK</td>
      <td>1.67</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>IRAO</td>
      <td>ИнтерРАОао</td>
      <td>IRAO</td>
      <td>1.51</td>
      <td>3</td>
    </tr>
    <tr>
      <th>33</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>RUAL</td>
      <td>РУСАЛ ао</td>
      <td>RUAL</td>
      <td>1.45</td>
      <td>3</td>
    </tr>
    <tr>
      <th>26</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>OZON</td>
      <td>OZON-адр</td>
      <td>OZON</td>
      <td>1.40</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>ALRS</td>
      <td>АЛРОСА ао</td>
      <td>ALRS</td>
      <td>1.34</td>
      <td>3</td>
    </tr>
    <tr>
      <th>19</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>MOEX</td>
      <td>МосБиржа</td>
      <td>MOEX</td>
      <td>1.33</td>
      <td>3</td>
    </tr>
    <tr>
      <th>17</th>
      <td>IMOEX</td>
      <td>2024-06-11</td>
      <td>MAGN</td>
      <td>ММК</td>
      <td>MAGN</td>
      <td>1.32</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Function for downloading shares' history in standard manner
import pandas as pd 
from tqdm import tqdm
def shares_history(isin): 
    
    df_full = pd.DataFrame()
    cond = True
    k=0
    while cond:    
        url = 'https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/{}.html?iss.only=history&marketprice_board=1&from=2023-01-01&limit=100&start={}'.format(isin,k)
        df = pd.read_html(url,encoding = 'utf-8')[0]
        df.columns = [i.split(' ')[0] for i in df.columns]
        if df.empty: 
            cond = False
           
        else:
            df_full = pd.concat([df,df_full],axis=0)
            k+=100
    df_full = df_full.drop_duplicates()
    return df_full 
```


```python
## Execution of standard download

import time

start_time_pd = time.time()
usual_history = pd.DataFrame()
for j in tqdm(range(len(stocks))):
    stock = stocks[j]
    stock_df = shares_history(stock)
    usual_history = pd.concat([usual_history,stock_df],axis=0)
end_time_pd = time.time() - start_time_pd  
```

    100%|███████████████████████████████████████████| 20/20 [00:27<00:00,  1.36s/it]



```python
## Execution of package function

start_time_lib = time.time()
hist_prices = iss.history_prices(engine = 'stock',market = 'shares',isin = stocks,date = '2023-01-01',show_progress=True)
hist_prices.head()

end_time_lib = time.time() - start_time_lib 
```

    Fetching data: 100%|████████████████████████████| 20/20 [00:03<00:00,  6.43it/s]



```python
print(f'Execution time of standard requests: {round(end_time_pd,3)} seconds')
print(f'Execution time of package function: {round(end_time_lib,3)} seconds')
```

    Execution time of standard requests: 27.137 seconds
    Execution time of package function: 3.114 seconds


Thus, the package function **is 9 times faster** than the standard request. This advatange was reached by using asynchronous framework
