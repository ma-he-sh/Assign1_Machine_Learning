# Assign1_SOFE4620U
Assignment1: Collecting Datasets 

For this assignment I decided collect historic cryptocurrency data from `coinmarketcap.com` and export 
it to a json and csv file. My goal of collecting historical data is to predict future change in the market 
value. Different coin types can be included to get their historical data. 

## Settingup the repo
```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How I request data from `coinmarketcap.com`
```sh
URL = "https://coinmarketcap.com/currencies/{COIN}/historical-data/?start={START_DATE}&end={END_DATE}"

{END_DATE}   => todays date
{START_DATE} => `coinmarketcap.com` only provide historic data upto 2013-04-28
```

## Scraping the data
```sh
cd scrapebc/api/
python scrape.py
```

## Adding additional cryptocurrency types to extract historical data
```sh
goto => /scrapebc/api/

Add new coins to array;
COIN_TYPE = [
    "bitcoin",
    "ethereum",
    "ripple",
    "litecoin"
]
```

## Storing the scraped data :: JSON and CSV
```sh
Scraped data is stored in /scrapebc/api/csv_data and /scrapebc/api/json_data folders.
```


