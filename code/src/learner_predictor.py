'''
Created on Oct 29, 2015

@author: rags1_000
'''
import pandas as pd
import numpy as np
import scipy.io
ctrain=pd.read_csv(r"C:\kaggle competitions\rossman store sales\complete_train.csv")

a=[]
temp=ctrain.loc[ctrain["StoreType"]=="a"]
avg=temp["Customers"].mean()
a.append(avg)
temp=ctrain.loc[ctrain["StoreType"]=="b"]
avg=temp["Customers"].mean()
a.append(avg)
temp=ctrain.loc[ctrain["StoreType"]=="c"]
avg=temp["Customers"].mean()
a.append(avg)
temp=ctrain.loc[ctrain["StoreType"]=="d"]
avg=temp["Customers"].mean()
a.append(avg)

scipy.io.savemat(r"C:\kaggle competitions\rossman store sales\CustVSStoreType.mat",mdict={'avg1':a})

a=[]
temp=ctrain.loc[ctrain["Assortment"]=="a"]
avg=temp["Customers"].mean()
a.append(avg)
temp=ctrain.loc[ctrain["Assortment"]=="b"]
avg=temp["Customers"].mean()
a.append(avg)
temp=ctrain.loc[ctrain["Assortment"]=="c"]
avg=temp["Customers"].mean()
a.append(avg)

scipy.io.savemat(r"C:\kaggle competitions\rossman store sales\CustVSAssortment.mat",mdict={'avg2':a})

a=[]
temp=ctrain.loc[ctrain["Promo"]==1]
avg=temp["Customers"].mean()
a.append(avg)
temp=ctrain.loc[ctrain["Promo"]==0]
avg=temp["Customers"].mean()
a.append(avg)
scipy.io.savemat(r"C:\kaggle competitions\rossman store sales\CustVSPromo.mat",mdict={'avg3':a})

print len(ctrain["CompetitionDistance"].unique())

print ctrain["PromoInterval"].unique()

