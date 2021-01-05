# End to end flight price predictor

In this project I created a web application that can predict fare of a flight. 

![Screenshot (52)](https://user-images.githubusercontent.com/54037847/103127160-b1729200-46b6-11eb-85b5-5e3ffcf179cb.png)

![Screenshot (53)](https://user-images.githubusercontent.com/54037847/103127299-365dab80-46b7-11eb-8540-01e8be26f2b5.png)


This app is currently live and can be found at: https://flight-fare-predictor-flask.herokuapp.com/

This project looks into various Python-based machine learning and data science libraries in an attempt to build a machine learning model capable of predicting price of a flight.
This repository was created to help clarify how to utilise flask and gunicorn to easily deploy a python machine learning model as a web app on Heroku.
The trained model achieved accuracy of more than 95% on the test set and its weights have been saved in the very useful HDF5 format. 

### we are going to take following approch:

#### 1. problem defination 
Problem Build a system capable of predicting fare of a flight.

#### 2. data 
Original data came from the kaggle competition https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh/

#### 3. Data preprocessing and EDA

#### 4. Creating a model
I buid two models 
1. XGboost
2. Random Forest

### Deployment
For deploying my web application I used Flask framework and deployed it on heroku.
