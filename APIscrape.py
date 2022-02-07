import requests
import pandas as pd
import time
from datetime import datetime,timedelta

apiUrl='http://api.pro.coinbase.com'
sym='BTC-USD'
barSize='300'
timeEnd=datetime.now()
delta=timedelta(minutes=5)
timeStart=timeEnd-(300*delta)
timeEnd=timeEnd.isoformat()
timeStart=timeStart.isoformat()

parameters={'start':timeStart,
			'end':timeEnd,
			'granularity':barSize}
data=requests.get(f'{apiUrl}/products/{sym}/candles',
					params=parameters,
					headers={'content-type':'application/json'})

df=pd.DataFrame(data.json(),
				columns=['time','low','high','open','close','volume'])
df['date']=pd.to_datetime(df['time'],unit='s')
df=df[['time','open','high','low','close']]
print(df)