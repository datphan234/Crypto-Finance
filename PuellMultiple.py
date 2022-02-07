import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('btcprice.csv')
df['date']=pd.to_datetime(df['date'])


df.sort_values(by='date',inplace=True)
df.reset_index(inplace=True,drop=True)
df.reset_index(inplace=True)

df['btcissuance']=7200/2**(np.floor(df['index']/1458))
df['usdissuance']=df['btcissuance']*df['value']
df['MAusdissuance']=df['usdissuance'].rolling(window=365).mean()
df=df[df['date']>'2010-12-31']

fig,ax1=plt.subplots()
ax2=ax1.twinx()

ax1.fill_between(df['date'],4,10,color='red',alpha=.4)
ax1.fill_between(df['date'],.3,.6,color='green',alpha=.4)

ax1.semilogy(df['date'],df['usdissuance']/df['MAusdissuance'],color='darkred',alpha=.8)
ax2.semilogy(df['date'],df['value'])


ax1.yaxis.set_major_formatter('{x:.1f}')
ax1.yaxis.set_minor_formatter('{x:.1f}')
#ax2.yaxis.set_minor_formatter()

ax1.set_ylabel('Puell')
ax2.set_ylabel('BTC Price')
plt.title('BTC Puell Multiple')

plt.show()
print(df)