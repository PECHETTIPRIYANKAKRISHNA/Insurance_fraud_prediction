# Insurance_fraud_prediction

Using Classification Techniques ,Data preprocessing ,Feature Engineering,Feature Extraction and classification algorithms from Machine Learning we Predict which claim is genuine and which claim is fraud.

# EXPLORATORY DATA ANALYSIS(EDA)
Here in EDA,we perform data cleaning techniques and visualize the data.Considering result as output variable and all the variables as input variables,we visualize the result data.
![image](https://user-images.githubusercontent.com/98581209/167898125-32cc7a92-ba5e-4078-8ea4-3eb4ef5839b2.png)

Next, We try to map the categorical data from our easy understanding.

And we balance the data using Random oversampler.The balanced data is as follows:
![image](https://user-images.githubusercontent.com/98581209/167898794-8e5a1f08-7c0d-42e1-bfe2-c6938f1cafad.png)

# MODEL BUILDING
We perform different model building techniques like logistic regression,Decision Tree,Random Forest,Adaboost etc.,. and try to predict algorithm which gives the maximum training and testing accuracy i.e, 99% and 86% respectively.

As Random forest is giving highest accuracy we use this model for our deployment.

# DEPLOYMENT
We load the data in pickle file and use this data for our deployment purpose.We use streamlit for our deployment purpose.

The output of streamlit will be as follows

GENUINE PREDICTION
<img width="346" alt="genuine prediction" src="https://user-images.githubusercontent.com/98581209/167900797-25d0b4ab-df85-43e1-9e22-0c92e7e5cc66.png">

FRAUD PREDICTION
<img width="317" alt="fraud prediction" src="https://user-images.githubusercontent.com/98581209/167900848-05ba60df-b46a-4a54-a438-4586e6144911.png">

Thankyou for reading!!!
