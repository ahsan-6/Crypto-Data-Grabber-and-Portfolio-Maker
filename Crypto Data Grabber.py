import pandas as pd
import requests

r=requests.get('https://api.wazirx.com/api/v2/tickers')
data=r.json()
df=pd.DataFrame(data)
df2=pd.read_excel("Crypto.xlsx")
tickers= list(df2.index)

for i in tickers:
    df2['Last'][i]=df[i]['last']
    df2['Profit/Loss'][i]=(df2['Last'][i]-df2['Average'][i])*df2['Holdings'][i]
