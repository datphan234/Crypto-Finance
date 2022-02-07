import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

#portfolios
port1={'SPY':'100'}
port2={'SPY':'95','BTC-USD':'5'}
port3={'BTC-USD':'100'}
port4={'BTC-USD':'30','TSLA':'70'}
port5={'BTC-USD':'70','ETH-USD':'30'}
port6={'BTC-USD':'60','ETH-USD':'20','TSLA':'20'}

members=['BTC-USD','ETH-USD','SPY','TSLA']

#Portfolio Calculation
def PortfolioCalc(weightings, data, name):
	data[name]=sum([int(weightings[x])*data[x]/100 for x in list(weightings.keys())])
	return data


#datatable
basedata=yf.Ticker(members[0]).history(period='max').reset_index()[['Date','Open']]
basedata['Date']=pd.to_datetime(basedata['Date'])
basedata=basedata.rename(columns={'Open':members[0]})

if(len(members)>1):
	for x in range(1,len(members)):
		newdata=yf.Ticker(members[x]).history(period='max').reset_index()[['Date','Open']]
		newdata['Date']=pd.to_datetime(newdata['Date'])
		newdata=newdata.rename(columns={'Open':members[x]})
		basedata=pd.merge(basedata,newdata,on='Date')

basedata=basedata[basedata['Date']>'2020-01-01']

for x in members:
	basedata[x]=basedata[x]/(basedata[x].iloc[0])

basedata=PortfolioCalc(port1,basedata,'port1')
basedata=PortfolioCalc(port2,basedata,'port2')
basedata=PortfolioCalc(port3,basedata,'port3')
basedata=PortfolioCalc(port4,basedata,'port4')
basedata=PortfolioCalc(port5,basedata,'port5')
basedata=PortfolioCalc(port6,basedata,'port6')

print(basedata)

#plt.plot(basedata["Date"], basedata["port1"], label = "100% s&p500")
#plt.plot(basedata["Date"], basedata["port2"], label = "95% s&p500, 5% BTC")
#plt.plot(basedata["Date"], basedata["port3"], label = "100% BTC")
plt.plot(basedata["Date"], basedata["port4"], label = "30% BTC, 70% TLSA")
plt.plot(basedata["Date"], basedata["port5"], label = "70% BTC, 30% ETH")
plt.plot(basedata["Date"], basedata["port6"], label = "60% BTC, 20% ETH, 20% TSLA")
plt.legend(loc='upper left')
plt.show()

