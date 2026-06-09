import pandas as pd
import numpy as np

pk=pd.read_csv("D:\project\employees.csv")
#print(pk.head(10))
pk["COMMISSION_PCT"]=pk["SALARY"]*0.10
pk.loc[9,"MANAGER_ID"]=121
pk["city"]=["karachi","nowshera","risalpur","lahore","peshawer"]+[None]*45
#print(pk.head())
#pk.to_csv("data")
#pk.to_csv("DATAFRAME")
#print(pk)
pk.drop(columns="city",inplace=True)
pk.insert(2,"pay",[200,800,900,400]+[None]*46)
pk.insert(3,"hours",[1,3,4,2]+[None]*46)
print(pk.head(4))
pk.head(4).to_csv("clean data")
print(pk)


#print(pk.info())
#print(pk.describe())
#print(pk.isna().sum())











