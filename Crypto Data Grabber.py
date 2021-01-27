import pandas as pd
import requests

r=requests.get('https://api.wazirx.com/api/v2/tickers')
df2=pd.read_excel("Crypto.xlsx",engine="openpyxl",index_col='Ticker')
tickers= list(df2.index)

for i in tickers:
    df2['Last'][i]=r.json()[i]['last']
df2.to_excel("Crypto.xlsx")
