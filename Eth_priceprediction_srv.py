#Description: This program attempts to prdeict the price of ETH by SVR

import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


#Read the data
df=pd.read_csv('gemini_ETHUSD_day.csv')
df=df.iloc[::-1]
df=df.drop(['Volume','High','Low','Symbol','Open','Unix Timestamp'], axis=1)
df=df.set_index(pd.DatetimeIndex(df['Date'].values))



future_days=5

#New column
df[str(future_days)+'_Day_Price_Forecast']=df[['Close']].shift(-future_days)
print(df[['Close',str(future_days)+'_Day_Price_Forecast']])

X=np.array(df[['Close']])
X=X[:df.shape[0]-future_days]
#print(X)

y=np.array(df[str(future_days)+'_Day_Price_Forecast'])
y=y[:-future_days]
#print(y)

#Split the data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y, test_size=0.2)

from sklearn.svm import SVR
svr_rbf=SVR(kernel='rbf',C=1e3,gamma=0.00001)
svr_rbf.fit(x_train, y_train)

svr_rbf_confidence = svr_rbf.score(x_test,y_test)
#print('svr_rbf accuracy:',svr_rbf_confidence)

svm_prediction = svr_rbf.predict(x_test)
#print(svm_prediction)

#print(y_test)
plt.figure(figsize=(12,4))
plt.plot(svm_prediction,label='Prediction',lw=2,alpha=.7)
plt.plot(y_test,label='Reality',lw=2,alpha=.7)
plt.title('ETH Prediction vs Reality (5 days ahead)')
plt.ylabel('ETH Price in USD')
plt.xlabel('Time')
plt.legend(loc='upper right')
plt.show()
