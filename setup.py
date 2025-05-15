from setuptools import setup, find_packages

setup(
    name='ISSMOEX',
    version='1.1.5',
    packages=find_packages(),
    install_requires=[
        'asyncio',
        'aiohttp',
        'pandas',
        'nest_asyncio',
        'tqdm'
    ],
    url='https://github.com/alexandrettto/issmoex',
    license='MIT',
    author='Illyuk Alexander',
    author_email='aaillyuk@gmail.com',
    description='A package to interact with the MOEX ISS API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
