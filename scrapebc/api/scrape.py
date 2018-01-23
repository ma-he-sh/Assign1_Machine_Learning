# -*- coding: utf-8 -*-

"""
    Import Libraries
"""
import pandas as pd
import datetime
import json
import csv
import os
from config import URL, COIN_TYPE, CSV_dir, JSON_dir

def _save_json(jsondata, coin_type):
    """
        Create folder if not exists and
        save the formatted JSON data
    """

    if not os.path.exists(JSON_dir):
        os.makedirs(JSON_dir)

    file_name = JSON_dir+coin_type+".json"
    
    with open(file_name, "wb") as f:
        f.write(json.dumps(jsondata, indent=4))

def _save_csv(data, coin_type):
    """
        Create folder if not exists and
        save data as csv
    """

    if not os.path.exists(CSV_dir):
        os.makedirs(CSV_dir)

    #create a row to insert
    header_row = ["Date", "Open", "High", "Low", "Close", "Volume", "Market"]
    rows = zip(data["date"], data["open"], data["high"], data["low"], data["close"], data["volume"], data["market"])

    file_name = CSV_dir+coin_type+".csv"

    with open(file_name, "wb") as f:
        w = csv.writer(f)
        w.writerow(header_row)
        for row in rows:
            w.writerow(row)

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
    _save_csv(col_data, coin_type)

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