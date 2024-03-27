## Linear Regression 
The classic regression problem involves a single independent variable and a dependent variable. This is called simple regression. This component supports simple regression.

Multiple linear regression involves two or more independent variables that contribute to a single dependent variable. Problems in which multiple inputs are used to predict a single numeric outcome are also called multivariate linear regression.

The Linear Regression component can solve these problems, as can most of the other regression components.

Multi-label regression is the task of predicting multiple dependent variables within a single model. For example, in multi-label logistic regression, a sample can be assigned to multiple different labels. (This type of regression is not supported in Azure Machine Learning. To predict multiple variables, create a separate learner for each output that you wish to predict..)

There are two methods of loss functions used to fit the regression line: A. ordinary least squares(OLS) method, and B. gradient descent.

### Ordinary least squares (OLS):
this loss function computes error as the sum of the square of distance from the actual value to the predicted line, and fits the model by minimizing the squared error. This method assumes a strong linear relationship between the inputs and the dependent variable. This is usually used for small datasets.

∑(yi – ŷi)^2 - where yi is the actual value and ŷi is the predicted value.

R-squared : R-squared is a statistical measure of how close the data are to the fitted regression line. It indicates the proportion of the variance in the dependent variable that is predictable from the independent variable(s).

    Training settings:-
    Solution method - OLS
    L2 regularization weight - 0.001 (Non-zero is recommened to avoid overfitting)
    Random number seed - 123

### Gradient descent: 
This method minimizes the amount of error at each step of the model training process. There are many variations on gradient descent and its optimization for various learning problems has been extensively studied. If you choose this option for Solution method, you can set a variety of parameters to control the step size, learning rate, and so forth. This option also supports use of an integrated parameter sweep. This is used for more complex dataset.

     Training settings:-
     Solution method - Gradient descent
     L2 regularization weight - 0.001 (Non-zero is recommened to avoid overfitting)
     Random number seed - 123
     Learning rate - 0.01
     Number of training epochs - 100
     Create Trainer mode - Single Parameter Sweep or Parameter Range Sweep

Reference - https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/linear-regression?view=azureml-api-2#create-a-regression-model-using-ordinary-least-squares
     
