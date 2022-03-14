#Description: Predict the price of ETH

#Libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Load and clean the data
df=pd.read_csv('gemini_ETHUSD_day.csv')
df=df.iloc[::-1]
df=df.drop(['Volume','High','Low','Symbol','Open','Unix Timestamp'], axis=1)
#print(df)

#Create a variable for predicting 'n' days
projection=14

#Create prediction column
df['Prediction']=df[['Close']].shift(-projection)
#print(df)

#Create the independent data set (X)
X=np.array(df[['Close']])
X=X[:-projection]

#Create the dependent data set (y)
y=df['Prediction'].values
y=y[:-projection]

#Split the data into 85% training, 15% testing
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=.15)

#Create and train the model
LinReg = LinearRegression()
LinReg.fit(x_train, y_train)

#Test the model using score
LinReg_confidence = LinReg.score(x_test, y_test)
print('Linear regression confidence:',+ LinReg_confidence)

#Create  a variable x_projection for the last 14 days
x_projection=np.array(df[['Close']])[-projection:]

#Linear Regression models predictions
LinReg_prediction=LinReg.predict(x_projection)

#Final prediction
df1=pd.DataFrame(x_projection,LinReg_prediction)
print(df1)








