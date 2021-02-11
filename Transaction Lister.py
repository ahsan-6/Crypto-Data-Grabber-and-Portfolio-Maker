import pandas as pd
import requests
import datetime

r=requests.get('https://api.wazirx.com/api/v2/tickers')
tran_df=pd.read_excel("Transactions.xlsx",engine="openpyxl")

def tt_func(x):
    if x=='b':  return 'buy'
    else : return 'sell'

choice=input('Have transactions to add (y/n)=')
while(choice.lower()=='y'):
    ticker=input("Enter ticker=")
    tt_var=input("Type of transaction (b/s)=")
    volume=float(input("Enter quantity bought/sell="))
    price=float(input("Enter price="))
    
    tran_df.loc[len(tran_df.index)] = [ticker, volume, price,tt_func(tt_var)]

    choice=input("Have more transactions to add y/n=")

tran_df.to_excel("Transactions.xlsx",index=False)