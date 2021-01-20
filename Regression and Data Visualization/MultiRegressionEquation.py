import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn import linear_model
from pathlib import Path


datapath = Path("StudentsPerformance.csv")
print(datapath.exists())
data = pd.read_csv(datapath)
processdata = data.dropna()  # You this to drop the NAN
print(processdata)
# Multivariated Regression
# X values are the independent variables
X = data.head()[['reading score']]
Y = data.head()['math score']

# sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)
print('Intercept:\n', regr.intercept_)
print('Coefficents:\n', regr.coef_)

# to display full statistical mode
X = sm.add_constant(X)  # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
