import pandas as pd
t=pd.read_csv('titanictrain.csv')
t.head(5)
import pandas as pd
t=pd.read_csv('titanictrain.csv')
t.describe()
import pandas as pd
t=pd.read_csv('titanictrain.csv')
t.drop(['SibSp','Ticket'],axis=1,inplace=True)
t.head(5)

t['Cabin']=t['Cabin'].fillna("xxx")
t.head(5)

import seaborn as sns
import matplotlib.pyplot as plt
ax=sns.countplot(x="Pclass",hue="Survived",palette="Set1",data=t)
ax.set(title="Passenger status against passenger class",xlabel="Pclass",ylabel="Total")
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
ax=sns.countplot(x="Sex",hue="Survived",palette="Set2",data=t)
ax.set(title="Survival rate of men vs women",xlabel="Sex",ylabel="Total")
plt.show()

interval=[5,13,18,60,120]
categories=['Children','Teen','Adult','Senior Citizen']
t['age']=pd.cut(t['Age'],interval,labels=categories)
ax=sns.countplot(x="age",hue="Survived",palette="Set1",data=t)
ax.set(title="Survival rate acc to age",xlabel="Age",ylabel="Total")
plt.show()
	
