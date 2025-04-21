import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('HRPDataset.csv')
print(df.head(5))

print('Defining x and y variables')
x=df['Area']
y=df['Price']

plt.scatter(x,y,color='blue')

print('Splitting the dataset into Training data and Testing data')
x_train,x_test,y_train,y_test= train_test_split(x,y,random_state=0,test_size=0.20)

plt.scatter(x_train,y_train,color='green')

plt.scatter(x_test,y_test,color='red')

x_train.shape

print('Training the model using x_train and y_train')
lr=LinearRegression()
lr.fit(x_train.values.reshape(-1,1),y_train)

print('Linear Model coeeficient(m):',lr.coef_)
print('Linear Model coeeficient(m):',lr.intercept_)

print('Predicting using the the trained model of x_test')
y_pred=lr.predict(x_test.values.reshape(-1,1))

print(y_test)

print(y_pred)

plt.scatter(x_train,y_train,color='blue')
plt.scatter(x_test,y_pred,color='purple')

from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))
