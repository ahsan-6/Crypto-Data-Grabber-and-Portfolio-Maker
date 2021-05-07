import pandas as pd
import requests

r=requests.get('https://api.wazirx.com/api/v2/tickers')
tran_df=pd.read_excel("Transactions.xlsx",engine='openpyxl')
crypto_df=pd.DataFrame(columns=['Ticker','Last','Average','Quantity','Cost','Profit/Loss','P/L%'])
crypto_df.set_index('Ticker',inplace=True)

for i in range(len(tran_df.index)):
    tick=tran_df['Ticker'][i]
    if tick in list(crypto_df.index):       # re-entry
        crypto_df.loc[tick,'Last']=float(r.json()[tick]['last'])
        if (tran_df['Type'][i].lower()=='buy'):
            crypto_df.loc[tick,'Average']=(crypto_df['Cost'][tick]+tran_df['Cost'][i])/(crypto_df['Quantity'][tick]+tran_df['Quantity'][i])
            crypto_df.loc[tick,'Quantity']+=tran_df['Quantity'][i]
        else:
            crypto_df.loc[tick,'Quantity']-=tran_df['Quantity'][i]
    else:                                   # initial entry
        crypto_df.loc[tick]=[r.json()[tick]['last'],(tran_df['Cost'][i]/tran_df['Quantity'][i]),tran_df['Quantity'][
            i],tran_df['Cost'][i],0,0]

#if quantity 0 then drop the ticker row

for tick in list(crypto_df.index):
    if float(crypto_df['Quantity'][tick])==0.0 :
        crypto_df.drop(tick,inplace=True)
    else:
        crypto_df.loc[tick,'Profit/Loss']=(float(crypto_df['Last'][tick])-float(crypto_df['Average'][tick]))*crypto_df['Quantity'][tick]
        crypto_df.loc[tick,'P/L%']=(crypto_df['Profit/Loss'][tick]/(crypto_df['Quantity'][tick]*crypto_df['Average'][tick]))*100

print(crypto_df)
crypto_df.to_excel('Portfolio.xlsx')