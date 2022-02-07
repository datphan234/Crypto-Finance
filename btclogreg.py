import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#data processing
df=pd.read_csv('btc_price.csv')
df=df[df['value']>0]
df=df.iloc[::-1]
df['date']=pd.to_datetime(df['date'])

#this is the function we want to fit over our data: a.log(x)+b
#we need to find appropriate coefficients
def func(x, p1, p2):
    return p1*np.log(x) + p2

#we are fitting log of price of BTC against the function, not actual price
ydata = np.log(df['value'])
xdata = np.array([x+1 for x in range(len(df))]) #just use numbers for dates

#extract optimal coefficients using curve fit
popt, pcov = curve_fit(func, xdata, ydata, p0=(3.0, -10))



#try to get ydata from xdata and function
#popt has coefficients, pcov has covariances between them
print(df)

#generate fitted Y data
fittedYdata = func(xdata, popt[0], popt[1]) #pass values to function

#plot
#plt.style.use("dark_background")
plt.semilogy(df["date"], df["value"])


for i in range(-3,6):
    plt.plot(df["date"], np.exp(fittedYdata+i)) #exponentiate the data
   # plt.fill_between(df['date'],np.exp(fittedYdata+i-1),np.exp(fittedYdata+i),alpha=.4)



plt.title('BTC logarithmic regression')
plt.ylim(bottom=0.1)
plt.axhline(y=1000,xmin=0,xmax=1,color='r', linewidth=.1)
plt.axhline(y=10000,xmin=0,xmax=1,color='r',linewidth=.1)
plt.axhline(y=100,xmin=0,xmax=1,color='r',linewidth=.1)
plt.show()
