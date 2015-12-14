'''
Created on Oct 19, 2015

@author: rags1_000
'''
import pandas as pd
import math
import datetime
import numpy as np
from datetime import timedelta
from itertools import count
train=pd.read_csv(r"/media/raghu/DATA/Rossman-Store-sales/data/train.csv")


store=pd.read_csv(r"/media/raghu/DATA/Rossman-Store-sales/data/store.csv")
store["CompetitionOpenSinceMonth"]=store["CompetitionOpenSinceMonth"].fillna(0)
store["CompetitionOpenSinceYear"]=store["CompetitionOpenSinceYear"].fillna(0)
store["CompetitionOpenSinceMonth"]=store["CompetitionOpenSinceMonth"].astype(int)
store["CompetitionOpenSinceYear"]=store["CompetitionOpenSinceYear"].astype(int)
#store["CompetitionStartDate"]=store.apply(lambda x:'%s-1-%s' %(np.round(x["CompetitionOpenSinceMonth"]),np.round(x["CompetitionOpenSinceYear"])),axis=1)
store["CompetitionStartDate"]=store.apply(lambda x :'%s-1-%s' %(x["CompetitionOpenSinceMonth"],x["CompetitionOpenSinceYear"]),axis=1)
store.loc[store["CompetitionStartDate"]=="0-1-0","CompetitionStartDate"]=None
store["CompetitionStartDate"]=store["CompetitionStartDate"].fillna(store["CompetitionStartDate"].mode())
store["CompetitionDistance"]=store["CompetitionDistance"].fillna(store["CompetitionDistance"].mean())
store["CompetitionStartDate"]=pd.to_datetime(store["CompetitionStartDate"])

store["Days"]=(store["Promo2SinceWeek"]-1)*7+1
store["Promo2SinceYear"]=store["Promo2SinceYear"].fillna(0)

store["Promo2SinceYear"]=store["Promo2SinceYear"].astype(int)
store["YearStartPromo2"]=store.apply(lambda x: "1-1-%s" %(x["Promo2SinceYear"]),axis=1)
store.loc[store["YearStartPromo2"]=="1-1-0","YearStartPromo2"]=None
s=store.ix[store["YearStartPromo2"]==None]
store["YearStartPromo2"]=pd.to_datetime(store["YearStartPromo2"])
store["YearStartPromo2"]=store["YearStartPromo2"].fillna(np.datetime64('1900-01-01'))
store["Days"]=store["Days"].fillna(0)
store["YearStartPromo2"]=store.apply(lambda x: x['YearStartPromo2']+datetime.timedelta(days=x['Days']),axis=1)
#store["Promo2StartDate"]=store.apply(DatetimeIndex(store["YearStartPromo2"])+pd.DateOffset(np.round(store["Days"]))
del store["CompetitionOpenSinceMonth"]
del store["CompetitionOpenSinceYear"]
del store["Promo2SinceWeek"]
del store["Promo2SinceYear"]
del store["Days"]
store=store.rename(columns={'YearStartPromo2':'Promo2StartDate'})
#print store["CompetitionStartDate"].value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)

store["CompetitionStartDate"]=store["CompetitionStartDate"].fillna(np.datetime64("2012-09-01"))       
print store.info()                                   
store.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/store1.csv",sep=',')

