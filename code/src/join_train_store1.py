'''
Created on Oct 26, 2015

@author: rags1_000
'''
import pandas as pd
train=pd.read_csv(r"C:\kaggle competitions\rossman store sales\train.csv")


store=pd.read_csv(r"C:\kaggle competitions\rossman store sales\store1.csv")

train_store=pd.merge(train,store,on="Store",how="outer")

print train_store.info()

train_store.to_csv(r"C:\kaggle competitions\rossman store sales\complete_train.csv",sep=',')

