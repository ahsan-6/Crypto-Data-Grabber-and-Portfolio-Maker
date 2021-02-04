import pandas as pd
import requests

r=requests.get('https://api.wazirx.com/api/v2/tickers')
df2=pd.read_excel("Crypto2.xlsx",engine="openpyxl",index_col='Ticker')
tickers= list(df2.index)

for i in tickers:
    if i in r.json():
            df2['Last'][i]=r.json()[i]['last']
    else: continue
df2.to_excel("Crypto2.xlsx")