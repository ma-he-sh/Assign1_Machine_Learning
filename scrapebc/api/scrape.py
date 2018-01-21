# -*- coding: utf-8 -*-

"""
    Import Libraries
"""
import pandas as pd
import datetime
import json
from config import URL, COIN_TYPE

def _save_json(jsondata, coin_type):
    """
        Save the formatted JSON data
    """
    file_name = coin_type+".json"
    
    with open(file_name, "w") as f:
        f.write(json.dumps(jsondata, indent=4))

def _req_coin_url(req_url, coin_type):
    """
        Getting content from url and reading data
    """
    ptable = pd.read_html(req_url)[0]
    col = list(ptable.columns.values)

    df = pd.DataFrame(ptable)

    """
        Organize the columns to lists for saving
        Data is stored in a dictionary
    """
    col_date = df['Date'].tolist()
    col_date = [x.encode('utf-8') for x in col_date]
    col_open = df['Open'].tolist()
    col_high = df['High'].tolist()
    col_low = df['Low'].tolist()
    col_close = df['Close'].tolist()
    col_volume = df['Volume'].tolist()
    col_market = df['Market Cap'].tolist()

    col_data = {
        "date": col_date,
        "open": col_open,
        "high": col_open,
        "low" : col_low,
        "close": col_close,
        "volume": col_volume,
        "market": col_market
    }

    jsondata = {
        "coin": coin_type,
        "coin_data": col_data
    }

    _save_json(jsondata, coin_type)

    #print col_market

if __name__ == "__main__":

    """
        Get current date and set the from date;
        Start date is set to 2013-04-28 & end date is set to todays date
    """
    td = datetime.date.today()
    start_date = "20130428"
    end_date = td.strftime("%Y%m%d")

    print start_date+" "+end_date

    """
        Construct the request URL and parse to scrape data
    """

    for c in xrange(len(COIN_TYPE)):

        print COIN_TYPE[c]

        req_url = (URL.format(COIN=COIN_TYPE[c], START_DATE=start_date, END_DATE=end_date))
        _req_coin_url(req_url, COIN_TYPE[c])