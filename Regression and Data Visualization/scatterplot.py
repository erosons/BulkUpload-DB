#  Numpy supports numerical and array operations
# Scipy
# Pandas support data manipulation and anlysis
#  Visulization Libraries, Matplotlib and seaborne,gmplot, plotly
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn import linear_model
from pathlib import Path


datapath = Path("StudentsPerformance.csv")
print(datapath.exists())
data = pd.read_csv(datapath)
print(data)
plt.scatter(data['math score'], data['reading score'], color='blue')
plt.title('Linear regression between math score and readings score', fontsize=14)
plt.xlabel('reading score', fontsize=14)
plt.ylabel('math score', fontsize=14)
plt.grid(False)
plt.show()
