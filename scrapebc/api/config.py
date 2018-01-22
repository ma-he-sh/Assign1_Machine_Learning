"""
    Configure file for requesting different bitcoins data
    Add coin name to COIN_TYPE
"""

#scrape url
URL = "https://coinmarketcap.com/currencies/{COIN}/historical-data/?start={START_DATE}&end={END_DATE}"

#request coin type
COIN_TYPE = [
    "bitcoin",
    "ethereum",
    "ripple",
    "litecoin"
]

# Data save directory
CSV_dir = "./csv_data/"
JSON_dir = "./json_data/"