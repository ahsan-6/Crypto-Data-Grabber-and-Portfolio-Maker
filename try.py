import pandas as pd

df=pd.read_excel("Transactions.xlsx",engine="openpyxl")
if (df['DateTime'][5]>df['DateTime'][3]):print("yes")
else:print("No")