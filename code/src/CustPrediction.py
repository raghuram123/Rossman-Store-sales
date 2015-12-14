# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:20:41 2015

@author: raghu
"""

from sys import argv

import pandas as pd
import os
import numpy as np
from sklearn.linear_model import LinearRegression, ridge
import sklearn.cross_validation
from sklearn.cross_validation import KFold
from sklearn.svm.libsvm import cross_validation
from sklearn.metrics import explained_variance_score
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import tree
from sklearn.grid_search import GridSearchCV
from multiprocessing.dummy import freeze_support
from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import SVR
from scipy.constants.constants import alpha
predictors = ["Promo", "Assortment", "CompetitionDistance", "StoreType", "Promo2", "Open"];
details=pd.read_csv(r"/media/raghu/DATA/Rossman-Store-sales/outputs/complete_train.csv")
details.loc[details["Assortment"]=="a","Assortment"]=1
details.loc[details["Assortment"]=="b","Assortment"]=2
details.loc[details["Assortment"]=="c","Assortment"]=3

details.loc[details["StoreType"]=="a","StoreType"]=1
details.loc[details["StoreType"]=="b","StoreType"]=2
details.loc[details["StoreType"]=="c","StoreType"]=3
details.loc[details["StoreType"]=="d","StoreType"]=4

details.loc[details["StateHoliday"]=="a","StateHoliday"]=1
details.loc[details["StateHoliday"]=="b","StateHoliday"]=2
details.loc[details["StateHoliday"]=="c","StateHoliday"]=3
#param_grid = {'learning_rate': [0.1, 0.05, 0.02, 0.01],
#                         'max_depth': [4, 5, 6],
#                        'min_samples_leaf': [3, 5, 9, 17],
#                        'max_features': [1.0, 2.0,3.0,4.0,5.0,6.0] 
#                    }
 

alg=AdaBoostRegressor(n_estimators=200,learning_rate=0.001,loss='square')
 
kf = KFold(details.shape[0], n_folds=3, random_state=1)
   
predictions = []
ctr=1;

for train, test in kf:
     train_predictors = (details[predictors].iloc[train,:])
     train_target = details["Sales"].iloc[train]
     alg.fit(train_predictors, train_target)
     test_predictions = alg.predict(details[predictors].iloc[test,:])
     predictions.append(test_predictions)
     print(ctr)
     ctr=ctr+1
predictions=np.concatenate(predictions);
cvscores= cross_val_score(alg, details[predictors], details["Customers"], cv=3)
print(cvscores.mean())
#
#gs_cv=GridSearchCV(alg, param_grid,n_jobs=4).fit(details[predictors], details["Customers"])
#print gs_cv.best_params_