import pandas as pd
import numpy as np

df = pd.read_csv('dataSet/StudentsPerformance.csv')
df.head()
df.info()
df.describe()

df2 = df.drop(['lunch','test preparation course'],axis=1,inplace = False)
df2.head(7)
df['parental level of education'] = df['parental level of education'].fillna('default')
df.head(8)

df['race/ethnicity'] = df['race/ethnicity'].map({
    'group A' : 'Asian',
    'group B' : 'African',
    'group C' : 'Afro-Asian',
    'group D' :'American'
})
df.head(8)

import seaborn as sns
import matplotlib.pyplot as plt

ax = sns.countplot(x='test preparation course', hue='gender', palette='Set1', data=df)
ax.set(title = 'Number of students who took up the test',
       xlabel = 'Course', ylabel = 'Total')
plt.show()
ax = sns.countplot(x='race/ethnicity', hue='gender', palette='Set2', data = df)
ax.set(title = 'Number of male/female',
       xlabel = 'Group', ylabel = 'Total')
plt.show()

interval = (0,40,60,75,110)
category = ['Fail','2nd Class','Ist Class','Distinction']
df['marks_cat'] = pd.cut(df.mathscore, interval, labels=category)
df.head()

ax = sns.countplot(data = df, x ='marks_cat', hue='gender')
ax.set(title='Category marks', xlabel = 'category', ylabel='total')
plt.show()

df['marks_cat'] = pd.cut(df['reading score'], interval, labels=category)
df.head()
ax = sns.countplot(data = df, x ='marks_cat', hue='gender')
ax.set(title='Reading score', xlabel = 'category', ylabel='total')
plt.show()

df.groupby('race/ethnicity').mean()
