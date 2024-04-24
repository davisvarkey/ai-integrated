# Introduction to ML and Supervised ML

Steps:
1. Data Exploration
2. Missing Value Imputatation
3. Feature Engineering
4. Modeling

Questions

1. How do you prevent the overfitting and complexity of a model? List down 4 techniques.
a. Regulaization techiques like L1, L2 regularization
b. Dimesionality reduction like PCA
c. Data augmentation techniques like SMOTE
d. Early stopping to prevent overfitting

2. Why cannot we use Linear Regression on categorical output?

3. You have a dataset of customer churn of an e-commerce company. There are 5 features namely: 
ip_address
total_order_count
total_order_value
average_rating_of_products_purchased
timestamp
	How would you use these features to train a classifier to predict if the customer would churn? Assume that you know the history of past customers whether they churned.

A. 

4. Provide examples when false positives are more important than false negatives, false negatives are more important than false positives, and when these two types of errors are equally important.

5. Case Study
Dataset - https://www.kaggle.com/mlg-ulb/creditcardfraud
Problem Statement - Build a machine learning pipeline to predict if a transaction using fraudulent from the given dataset
Task 1: Define the complete pipeline from data loading until prediction 
Task 2: Visualize different features to get a better sense of data. Explore at least 5 different types of plots.
Task 3: Does the dataset look skewed? What can be done to build a better model? Execute your assumptions 
Task 4: Execute dimensionality reduction to identify important features 
Task 5: Build at least 3 different ML models from among the following:
Logistic regression
Decision Tree
Random Forest
Gradient Boosting Trees
Adaboost
XGBoost
Naive Bayes
SVM
KNN
Task 6: Execute hyper-parameter tuning to improve the model performance 
Task 7: Evaluate models and identify the best model suited for the task 


There are two types of unsupervised machine learnig algorithms: K-means clustering and Anomaly detection. 

DBSCan clustering algorithm and isolation forests can be used for anomaly detection on this dataset.

DBScan clusters together closely packed points and marks outliers as noise. It doesn't require specifying the number of clusters in advance.


