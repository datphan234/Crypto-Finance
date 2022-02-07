import pandas as pd
import matplotlib.pyplot as plt
import ta

df=pd.read_csv('btcprice.csv')[['date','value']]
df['date']=pd.to_datetime(df['date'])
df=df[df['value']>0]
df=df.iloc[::-1]
print(df)

fig, [ax1,ax2] =plt.subplots(2,sharex=True)
ax1.semilogy(df['date'],df['value'])

df['rsi']=ta.momentum.rsi(close=df['value'],window=14)
ax2.plot(df['date'],df['rsi'])
plt.show()