# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 20:04:15 2015

@author: raghu
"""

import pandas as pd
import numpy as np

details=pd.read_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv")
#dic={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sept':9,'Oct':10,'Nov':11,'Dec':12}
#details.loc[details["Month1"]=="Jan","Month1"]=1
#details.loc[details["Month1"]=="Feb","Month1"]=2
#details.loc[details["Month1"]=="Mar","Month1"]=3
#
#details.loc[details["Month2"]=="Apr","Month2"]=4
#details.loc[details["Month2"]=="May","Month2"]=5
#details.loc[details["Month2"]=="Jun","Month2"]=6
#
#details.loc[details["Month3"]=="Jul","Month3"]=7
#details.loc[details["Month3"]=="Aug","Month3"]=8
#details.loc[details["Month3"]=="Sept","Month3"]=9
#
#details.loc[details["Month4"]=="Oct","Month4"]=10
#details.loc[details["Month4"]=="Nov","Month4"]=11
#details.loc[details["Month4"]=="Dec","Month4"]=12
#
#details.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv",sep=',')

#-----------------------------------------------------------------------------------------------

#details["Month1"]=details["Month1"].fillna(0)
#details["Month2"]=details["Month2"].fillna(0)
#details["Month3"]=details["Month3"].fillna(0)
#details["Month4"]=details["Month4"].fillna(0)
#details.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv",sep=',')

#-------------------------------------------------------------------------------------------------

#details["Promo2StartDate"]=pd.to_datetime(details["Promo2StartDate"])
#details.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv",sep=',')
#-------------------------------------------------------------------------------------------------

#details["tempyear"]=details["Date"].apply(lambda x: x.split('-')[0])
#details["Month1"]=details["Month1"].astype(int)
#details["Month1"]=details.apply(lambda x: "%s-1-%s" %(x["Month1"], x["tempyear"]),axis=1)
#
#details["Month2"]=details["Month2"].astype(int)
#details["Month2"]=details.apply(lambda x: "%s-1-%s" %(x["Month2"], x["tempyear"]),axis=1)
#
#details["Month3"]=details["Month3"].astype(int)
#details["Month3"]=details.apply(lambda x: "%s-1-%s" %(x["Month3"], x["tempyear"]),axis=1)
#
#details["Month4"]=details["Month4"].astype(int)
#details["Month4"]=details.apply(lambda x: "%s-1-%s" %(x["Month4"], x["tempyear"]),axis=1)
#
#details.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv",sep=',')
#-------------------------------------------------------------------------------------------------------

#details.loc[details["Promo2"]==0,"Month1"]=np.datetime64("1900-01-01")
#details.loc[details["Promo2"]==0,"Month2"]=np.datetime64("1900-01-01")
#details.loc[details["Promo2"]==0,"Month3"]=np.datetime64("1900-01-01")
#details.loc[details["Promo2"]==0,"Month4"]=np.datetime64("1900-01-01")

#
#details["Date"]=pd.to_datetime(details["Date"])
#details["Month1"]=pd.to_datetime(details["Month1"])
#details["Month2"]=pd.to_datetime(details["Month2"])
#details["Month3"]=pd.to_datetime(details["Month3"])
#details["Month4"]=pd.to_datetime(details["Month4"])
#details["Month1"]=details["Date"]-details["Month1"]
#details["Month2"]=details["Date"]-details["Month2"]
#details["Month3"]=details["Date"]-details["Month3"]
#details["Month4"]=details["Date"]-details["Month4"]
#details.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv",sep=',')

#-----------------------------------------------------------------------------------------------------------
#
#details["Month1"]=details["Month1"].apply(lambda x: x.split(' ')[0])
#details["Month2"]=details["Month2"].apply(lambda x: x.split(' ')[0])
#details["Month3"]=details["Month3"].apply(lambda x: x.split(' ')[0])
#details["Month4"]=details["Month4"].apply(lambda x: x.split(' ')[0])
#----------------------------------------------------------------------------------------------
#details.loc[details["Month1"]<0,"Month1"]=1000000
#details.loc[details["Month2"]<0,"Month2"]=1000000
#details.loc[details["Month3"]<0,"Month3"]=1000000
#details.loc[details["Month4"]<0,"Month4"]=1000000
#details["DaysSinceLastPromo2"]=details.loc[:,["Month1","Month2","Month3","Month4"]].min(axis=1)
#details.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv",sep=',')

#-----------------------------------------------------------------------------------------------------------------

#details.loc[details["Promo2"]==0,"DaysSinceLastPromo2"]=1000000
#details.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv",sep=',')