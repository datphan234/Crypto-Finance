import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


#BTC
btcdata=yf.Ticker('BTC-USD')
btcdata=btcdata.history(period='max').reset_index()[['Date','Open']]
#ETH
ethdata=yf.Ticker('ETH-USD')
ethdata=ethdata.history(period='max').reset_index()[['Date','Open']]
#BNB
bnbdata=yf.Ticker('BNB-USD')
bnbdata=bnbdata.history(period='max').reset_index()[['Date','Open']]
#SOL
soldata=yf.Ticker('SOL-USD')
soldata=soldata.history(period='max').reset_index()[['Date','Open']]
#LINK
linkdata=yf.Ticker('LINK-USD')
linkdata=linkdata.history(period='max').reset_index()[['Date','Open']]

#rename columns
btcdata=btcdata.rename(columns={'Date':'date','Open':'btc'})
ethdata=ethdata.rename(columns={'Date':'date','Open':'eth'})
bnbdata=bnbdata.rename(columns={'Date':'date','Open':'bnb'})
soldata=soldata.rename(columns={'Date':'date','Open':'sol'})
linkdata=linkdata.rename(columns={'Date':'date','Open':'link'})

#converting date
btcdata['date']=pd.to_datetime(btcdata['date'])
ethdata['date']=pd.to_datetime(ethdata['date'])
bnbdata['date']=pd.to_datetime(bnbdata['date'])
soldata['date']=pd.to_datetime(soldata['date'])
linkdata['date']=pd.to_datetime(linkdata['date'])

df=pd.merge(btcdata,ethdata, on='date')
df=pd.merge(df,bnbdata, on='date')
df=pd.merge(df,linkdata, on='date')


print('btc/eth spearman corr '+str(df['btc'].corr(df['eth'],method='spearman')))
print('btc/bnb spearman corr '+str(df['btc'].corr(df['bnb'],method='spearman')))
print('btc/link spearman corr '+str(df['btc'].corr(df['link'],method='spearman')))

print('btc/eth pearson corr '+str(df['btc'].corr(df['eth'],method='pearson')))
print('btc/bnb pearson corr '+str(df['btc'].corr(df['bnb'],method='pearson')))
print('btc/link pearson corr '+str(df['btc'].corr(df['link'],method='pearson')))