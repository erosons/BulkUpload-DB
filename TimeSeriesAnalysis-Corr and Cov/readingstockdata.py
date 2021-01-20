import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

start_date = datetime.datetime(2001, 1, 1)
end_date = datetime.datetime(2020, 6, 21)

#Getting Fianacial data from yahoo
all_data = {ticker: web.get_data_yahoo(ticker)["Adj Close"] for ticker in ["AAPL", "IBM", "GOOG", "MSFT"]}

stocker_data= web.DataReader(["AAPL", "IBM", "GOOG", "MSFT","GC=F"],"yahoo",start_date,end_date)["Adj Close"]
"""print(stocker_data)
print(stocker_data.pct_change()) #  to show percentage in the stock data

#plotting scattor plot visualization between IBN &  MSFT USING seaborn
#  show the trend line
sns.regplot("IBM","GC=F",stocker_data)
plt.title("%s Adj Close vs %s Adj Close prices" % ("IBM","GC=F"))
plt.show()

#plotting scattor plot visualization between IBN &  MSFT USING matplotlib
plt.scatter(stocker_data['IBM'], stocker_data['GC=F'], color='blue')
plt.title('Linear regression between IBM and GC=F', fontsize=14)
plt.xlabel('IBM', fontsize=14)
plt.ylabel('GC=F', fontsize=14)
plt.grid(False)
plt.show()"""

"""# to Show the correlation between  between to data points  e.g IBM and MSFT
show_corre=stocker_data.MSFT.corr(stocker_data["GC=F"])
print(show_corre)

#to show correlation for the entire data
show_all_data=stocker_data.corr()
print(show_all_data)"""
columns=stocker_data.columns
print(columns)

# plot perform a risk analysis plot on this stocks and check which to invest in
plt.scatter(stocker_data.mean(), stocker_data.std())
plt.xlabel("Expected returns")
plt.ylabel("Volatility or standard Deviation")
for label,x,y in zip(stocker_data.columns,stocker_data.mean(),stocker_data.std()):
    plt.annotate(label, 
                 xy=(x,y),xytext=(20,-20),
                 textcoords="offset points",ha='right', va='bottom',
                 bbox=dict(boxstyle="round",pad=0.5,fc="yellow",alpha=0.5),
                 arrowprops=dict(arrowstyle='->',ConnectionStyle="Arc3,rad=0"))
    plt.show()