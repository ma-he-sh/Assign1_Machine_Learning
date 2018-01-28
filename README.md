# Machine Learning and Data Mining
# Assign1_SOFE4620U
Assignment1: Collecting Datasets 

For this assignment I decided collect historic cryptocurrency data from `coinmarketcap.com` and export 
it to a json and csv file. My goal of collecting historical data is to predict future change in the market 
value. Different coin types can be included to get their historical data. 

## Setting up the repository
```sh
git clone git@github.com:Mahesh-Ranaweera/Assign1_SOFE4620U.git
cd Assign1_SOFE4620U

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Adding additional cryptocurrency types to extract historical data
```sh
goto => /scrapebc/api/config.py

Add new coins to array;
COIN_TYPE = [
    "bitcoin",
    "ethereum",
    "ripple",
    "litecoin",
    .....,
    .....
]
```

## Scraping the data
```sh
cd scrapebc/api/
python scrape.py
```

## Storing the scraped data as JSON and CSV
```sh
CSV DATA  => /scrapebc/api/csv_data 
JSON DATA => /scrapebc/api/json_data
```

---

## How I request data from `coinmarketcap.com`
```sh
URL = "https://coinmarketcap.com/currencies/{COIN}/historical-data/?start={START_DATE}&end={END_DATE}"

{END_DATE}   => todays date
{START_DATE} => `coinmarketcap.com` only provide historic data upto 2013-04-28
```


