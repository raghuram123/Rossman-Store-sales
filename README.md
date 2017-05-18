# Rossman-Store-sales

This is a Kaggle project https://www.kaggle.com/c/rossmann-store-sales
The data is placed in the "data directory". 

The full project problem specified in this link. 
https://www.kaggle.com/c/rossmann-store-sales

Data Directory:

The data directory contains all the input files. The description of these csv files are present in the above mentioned link itself. 

Code directory:

The code directory contains the following files in the same execution order. 

Basic Knowledge and exploratory data analysis:

https://www.kaggle.com/thie1e/rossmann-store-sales/exploratory-analysis-rossmann/notebook

https://www.kaggle.com/amhchiu/rossmann-store-sales/more-exploratory-data-analysis/run/84612/code

https://www.kaggle.com/ggep22/rossmann-store-sales/exploratory-analysis-day-level-patterns/notebook
1) store_feature_modulator.py
	This script does some feature modification in the given Store.csv file based on the above analysis. 
	Firstly, we are given two fields in the Store.csv file namely "CompetitionOpenSInceMonth" and "CompetitionOpenSinceYear". We combine these two together to form a "CompetitionStartDate" here. The dat is asumed to be the 1st of every month since its not given. 
	Similarly we find the "Promo2StartDate" which denotes the start date of promo2. For this we use the two fields "Promo2SinceWeek" and "Promo2SinceYear", using this a date is found out. 
	These are the main things done in this file so far. 

2)learner_predictor.py
This file simply does some data visualizations between sales three other fields. 

3)join_train_store1.py
This script joins the two training data files into a single file. A simple outer join is used. 

4)CustPrediction.py
This file does the prediction part. Further feature modification as well as proper usage of algorithm should be implemented to forecast the sales. 



		

