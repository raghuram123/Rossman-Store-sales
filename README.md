# Rossman-Store-sales

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. 

The project's challenge is to predict 6 weeks of daily sales for 1,115 stores located across Germany. Reliable sales forecasts enable store managers to create effective staff schedules that increase productivity and motivation

The Data source and the project is from kaggle.com. 

The description of the data is in the below mentioned link.

https://www.kaggle.com/c/rossmann-store-sales/data

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



		

