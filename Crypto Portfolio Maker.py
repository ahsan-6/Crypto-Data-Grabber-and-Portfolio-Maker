import pandas as pd
import requests

r=requests.get('https://api.wazirx.com/api/v2/tickers')
tran_df=pd.read_excel("Transactions.xlsx",engine='openpyxl')
crypto_df=pd.DataFrame(columns=['Ticker','Last','Average','Quantity','Profit/Loss','P/L%'])
crypto_df.set_index('Ticker',inplace=True)

for i in range(len(tran_df.index)):
    tick=tran_df['Ticker'][i]
    if tick in list(crypto_df.index):
        crypto_df.loc[tick,'Last']=float(r.json()[tick]['last'])
        if (tran_df['Type'][i].lower()=='buy'):
            crypto_df.loc[tick,'Average']=(crypto_df['Average'][tick]*crypto_df['Quantity'][tick]+tran_df['Price'][i]*tran_df['Quantity'][i])/(crypto_df['Quantity'][tick]+tran_df['Quantity'][i])
            crypto_df.loc[tick,'Quantity']+=tran_df['Quantity'][i]
        else:
            crypto_df.loc[tick,'Quantity']-=tran_df['Quantity'][i]
    else:
        crypto_df.loc[tick]=[r.json()[tick]['last'],tran_df['Price'][i],tran_df['Quantity'][i],0,0]

for tick in list(crypto_df.index):
    crypto_df.loc[tick,'Profit/Loss']=(float(crypto_df['Last'][tick])-float(crypto_df['Average'][tick]))*crypto_df['Quantity'][tick]
    crypto_df.loc[tick,'P/L%']=(crypto_df['Profit/Loss'][tick]/(crypto_df['Quantity'][tick]*crypto_df['Average'][tick]))*100

print(crypto_df)
crypto_df.to_excel('Portfolio.xlsx')