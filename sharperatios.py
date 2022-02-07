import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

timeperiod=365

df=pd.read_csv('gemini_BTCUSD_day.csv')
df=df.iloc[::-1]
df['Date']=pd.to_datetime(df['Date'])
df=df.rename(columns={'Open':'BTC'})
df=df.drop(['Volume','Low','Close','High','Symbol','Unix Timestamp'],axis=1)

eth=pd.read_csv('gemini_ETHUSD_day.csv')
eth=eth.iloc[::-1]
eth['Date']=pd.to_datetime(eth['Date'])
eth=eth.rename(columns={'Open':'ETH'})
eth=eth.drop(['Volume','Low','Close','High','Symbol','Unix Timestamp'],axis=1)


df=df.merge(eth,on='Date',how='right')

df['btcreturn']=100*(df['BTC']/df['BTC'].shift(timeperiod)-1)
df['ethreturn']=100*(df['ETH']/df['ETH'].shift(timeperiod)-1)

df['btcstd']=df['btcreturn'].rolling(timeperiod).std()
df['ethstd']=df['ethreturn'].rolling(timeperiod).std()

df['btcsharpe']=df['btcreturn']/df['btcstd']
df['ethsharpe']=df['ethreturn']/df['ethstd']

#plt.plot(df['Date'],df['btcsharpe'],label='btc')
#plt.plot(df['Date'],df['ethsharpe'],label='eth')
plt.plot(df['Date'],df['btcsharpe']-df['ethsharpe'],label='btcvseth')
#plt.plot(df['Date'],df['ethsharpe']-df['btcsharpe'],label='ethvsbtc')
plt.legend()
plt.axhline(y=0,xmin=0,xmax=1,color='r',label='price now')
plt.title('BTC vs ETH Sharpe Ratio')

plt.show()


print(df)