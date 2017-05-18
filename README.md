# Rossman-Store-sales

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. 

The project's challenge is to predict 6 weeks of daily sales for 1,115 stores located across Germany. Reliable sales forecasts enable store managers to create effective staff schedules that increase productivity and motivation

Files

train.csv - historical data including Sales
test.csv - historical data excluding Sales
sample_submission.csv - a sample submission file in the correct format
store.csv - supplemental information about the stores
Data fields

Most of the fields are self-explanatory. The following are descriptions for those that aren't.

Id - an Id that represents a (Store, Date) duple within the test set
Store - a unique Id for each store
Sales - the turnover for any given day (this is what you are predicting)
Customers - the number of customers on a given day
Open - an indicator for whether the store was open: 0 = closed, 1 = open
StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
StoreType - differentiates between 4 different store models: a, b, c, d
Assortment - describes an assortment level: a = basic, b = extra, c = extended
CompetitionDistance - distance in meters to the nearest competitor store
CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened
Promo - indicates whether a store is running a promo on that day
Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2
PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store

Code directory:

The code directory contains the following files in the same execution order. 

1) store_feature_modulator.py
	This script does some feature modification in the given Store.csv file. 
	Firstly, we are given two fields in the Store.csv file namely "CompetitionOpenSInceMonth" and "CompetitionOpenSinceYear". I combine these two together to form a "CompetitionStartDate" here. The date is asumed to be the 1st of every month since its not given. 
	Similarly I find the "Promo2StartDate" which denotes the start date of promo2. For this I use the two fields "Promo2SinceWeek" and "Promo2SinceYear", using this a date is found out. 

2)learner_predictor.py
This file simply does some data visualizations. 

3)join_train_store1.py
This script joins the two training data files into a single file. A simple outer join is used. 

4)CustPrediction.py
This file does the prediction part. Further feature modification as well as proper usage of algorithm should be implemented to forecast the sales. 



		

