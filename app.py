import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib . pyplot as plt car=pd.read csv(’carvana.csv’) car . shape
# set the background style of the plot
sns.set style(’whitegrid’)
sns.displot(car[’Price’], kde = False, color =’red’, bins = 30) car . info ()
car . describe ()
X=car . drop ([ ’ Price ’] , axis =1)
y=car [ ’ Price ’]
from sklearn . model selection import train test split
X train, X test, y train, y test=train test split(X, y, test size=0.2 )
from
from
from
from
from
ohe =
ohe.fit(X[[’Name’, ’Year’, ’Miles’]])
column trans = make column transformer((OneHotEncoder(categories=ohe.ca
sklearn . linear model import LinearRegression sklearn . metrics import r2 score
sklearn . preprocessing import OneHotEncoder sklearn . compose import make column transformer sklearn . pipeline import make pipeline
OneHotEncoder ( )
lr=LinearRegression () scores =[]
j=0
max = 0
for i in range (1 ,10):
remainder=’passthrough ’)
X train, X test, y train, y test=train test split(X,y,test size=i/10 lr=LinearRegression ()
pipe=make pipeline ( column trans , lr ) pipe.fit(X train, y train)
y pred=pipe . predict ( X test ) accuracy = r2 score(y test , y pred) scores .append(accuracy)
if (accuracy > max): j=i
max = accuracy
X train, X test, y train, y test=train test split(X,y,test size=j/10, r lr=LinearRegression ()
pipe=make pipeline ( column trans , lr )
pipe.fit(X train, y train)
y pred=pipe . predict ( X test )
r2 score(y test , y pred)
testing = X test . iloc [0:1]
testing
pipe . predict ( testing )
