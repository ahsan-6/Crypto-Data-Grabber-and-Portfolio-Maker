import pandas as pd
import requests

r=requests.get('https://api.wazirx.com/api/v2/tickers')
data=r.json()
df=pd.DataFrame(data)
df2=pd.read_excel("Crypto.xlsx",index_col='Ticker')
tickers= list(df2.index)

for i in tickers:
    df2['Last'][i]=df[i]['last']
df2.to_excel("Crypto.xlsx")