# -*- coding: utf-8 -*-
"""Customer_Churn_using_ANN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I0b4ohNpTN3Lp83O50x9FgvCpez8UWht
"""

import numpy as np
import pandas as pd

df=pd.read_csv('/content/customer_churn.csv')

df.info()

df.duplicated().sum()

df['Exited'].value_counts()

df.drop(['RowNumber','CustomerId','Surname'],axis=1,inplace=True)

df

df=pd.get_dummies(df,columns=['Geography','Gender'],drop_first=True)

df

from sklearn.model_selection import train_test_split

X=df.drop(columns=['Exited'])
Y=df['Exited']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=3)

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

X_train_scaled=scaler.fit_transform(X_train)
X_test_test=scaler.transform(X_test)

import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model=Sequential()

model.add(Dense(11,activation='relu',input_dim=11))
model.add(Dense(11,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['accuracy'])

history=model.fit(X_train_scaled,Y_train,epochs=100,validation_split=0.1)

model.layers[1].get_weights()

y_log=model.predict(X_test_test)

y_pred=np.where(y_log>0.5, 1, 0)

from sklearn.metrics import accuracy_score

accuracy_score(Y_test,y_pred)

import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

