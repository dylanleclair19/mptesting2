import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_and_save_data(ticker, filename):
    data = yf.download(ticker, period='1d')
    data['Date'] = datetime.now().strftime('%Y-%m-%d')
    data.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename))

if __name__ == '__main__':
    fetch_and_save_data('AAPL', 'data/data.csv')
