# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:20:41 2015

@author: raghu
"""

from sys import argv

import pandas as pd
import os
import numpy as np
import xgboost as xgb
from sklearn.linear_model import LinearRegression, ridge
import sklearn.cross_validation
from sklearn.cross_validation import KFold
from sklearn.svm.libsvm import cross_validation
from sklearn.metrics import explained_variance_score
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import tree
from itertools import product
from sklearn.grid_search import GridSearchCV
from multiprocessing.dummy import freeze_support
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error,r2_score
from scipy.constants.constants import alpha
predictors = ["Month","WeekOfYear","Promo2Indicator","Store","Promo", "Assortment", "CompetitionDistance", "StoreType","Open","DayOfWeek","StateHoliday","SchoolHoliday"];
traindata=pd.read_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv")
testdata=pd.read_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/teststore1.csv")
traindata=traindata.sort(["Date"],ascending=[True])
testdata=testdata.sort(["Date"],ascending=[True])
#details.loc[details["Assortment"]=="a","Assortment"]=1
#details.loc[details["Assortment"]=="b","Assortment"]=2
#details.loc[details["Assortment"]=="c","Assortment"]=3
#
#details.loc[details["StoreType"]=="a","StoreType"]=1
#details.loc[details["StoreType"]=="b","StoreType"]=2
#details.loc[details["StoreType"]=="c","StoreType"]=3
#details.loc[details["StoreType"]=="d","StoreType"]=4
#
#details.loc[details["StateHoliday"]=="a","StateHoliday"]=1
#details.loc[details["StateHoliday"]=="b","StateHoliday"]=2
#details.loc[details["StateHoliday"]=="c","StateHoliday"]=3
#details["DaysSinceCompetition"]=details["Date"]-details["CompetitionStartDate"]
#details.loc[details["Date"]==details["CompetitionStartDate"],"temp"]=0
#details.loc[details["temp"]<=0,"temp"]=0       
#details.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv",sep=',')
#
#details.loc[details["DaysSinceLastPromo2"]==1000000,"DaysSinceLastPromo2"]=0
#details.loc[details["Promo2"]==0,"DaysSinceLastPromo2"]=0
#details=details.sort(["Date"],ascending=[True])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
#traindata["Date"]=pd.to_datetime(traindata["Date"])
#testdata["Date"]=pd.to_datetime(testdata["Date"])
#traindata["WeekOfYear"]=traindata["Date"].apply(lambda x: x.week)
#testdata["WeekOfYear"]=testdata["Date"].apply(lambda x: x.week)
#testdata["Promo2Indicator"]=testdata["Promo2"]*testdata["DaysSinceLastPromo2"]
#traindata["Promo2Indicator"]=traindata["Promo2"]*traindata["DaysSinceLastPromo2"]
#testdata["Month"]=testdata["Date"].apply(lambda x: x.month)
#traindata["Month"]=traindata["Date"].apply(lambda x: x.month)
#traindata.loc[traindata["Promo2Indicator"]>0,"Promo2Indicator"]=1
#testdata.loc[testdata["Promo2Indicator"]>0,"Promo2Indicator"]=1

alg=RandomForestRegressor(n_estimators=1000 ,max_features=0.6,min_samples_split=20,min_samples_leaf=20,n_jobs=-1,random_state=1,oob_score=True)
alg.fit(traindata[predictors],traindata["Sales"])
predictions = []
testdata["Sales"]=alg.predict(testdata[predictors])
#for i in range(0,len(predictions)):
#    if(predictions[i]<=0):
#        predictions[i]=0
#    predictions[i]=round(predictions[i])

testdata["Sales"]=testdata["Sales"].apply(lambda x: round(x))
submission=pd.DataFrame({"Id":testdata["Id"],"Sales":testdata["Sales"]})
submission.sort(["Id"],ascending=True)
submission.to_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/submission.csv",sep=',',index=False)
#print(alg.n_estimators)
#print(alg.max_features)
#print(alg.min_samples_split)
#print(alg.min_samples_leaf)
#print(alg.n_jobs)
#print(alg.random_state)
#print("r2 score")
#print(r2_score(testdata["Sales"],predictions))
#cvscores= cross_val_score(alg, details[predictors], details["Sales"], cv=5)
#print(cvscores.mean())

#
#for train, test in kf: 
#     train_predictors = (details[predictors].iloc[train,:])
#     train_target = details["Sales"].iloc[train]
#     alg.fit(train_predictors, train_target)
#     test_predictions = alg.predict(details[predictors].iloc[test,:])
#     predictions.append(test_predictions)
#     print(ctr)
#     ctr=ctr+1
#predictions=np.concatenate(predictions,axis=0);


#gs_cv=GridSearchCV(alg, param_grid,n_jobs=4).fit(details[predictors], details["Customers"])
#print gs_cv.best_params_