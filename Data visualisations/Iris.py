import pandas as pd
import numpy as np
iris1=pd.read_csv('iris.csv')
iris1.head(5)
interval=[0,1,2,4]
category=['<1','1 to 2','>2']
iris1['Petal_cat']=pd.cut(iris1[' Petal_Width'],interval,labels=category)
ax=sns.countplot(hue="Class",palette="Set1",data=iris1,x="Petal_cat")
ax.set(title="Petal width",xlabel="cat of petal",ylabel="no. of flowers")
plt.show()


plt.figure(figsize=[12,6])
ax=sns.countplot(x=" Sepal_Width",palette="Set2",data=iris1[iris1['Class']=='Iris-virginica'])
ax.set(title="Iris-virginica",xlabel="Sepal width",ylabel="Total")
plt.show()
