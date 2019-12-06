import numpy as np
import pandas as pd

df = pd.read_csv('dataSet/BlackFriday.csv')
df.head()
df.info()
df.describe()

df2 = df.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'], axis=1, inplace = False)
df2.head()
df['City_Category'] = df['City_Category'].fillna('city')
df.head()
df['City_Category'] = df['City_Category'].map({
    'A': 'Metro Cities',
    'B': 'Small Towns',
    'C': 'Villages'
})

df.head()

df.rename(columns={
    'Product_Category_1':'Baseball Caps',
    'Product_Category_2':'Wine Tumblers',
    'Product_Category_3':'Pet Raincoats'
})

df['Marital_Status'] = df['Marital_Status'].map({
    0:'Unmarried',
    1:'Married'
})

df.head()

import seaborn as sns
import matplotlib.pyplot as plt

ax = sns.countplot(data = df, x = 'Product_Category_1', hue='Gender')
ax.set(title='Product 1', xlabel='category', ylabel='total')
plt.show()
ax = sns.countplot(data = df, x = 'Product_Category_2', hue='Gender')
ax.set(title='Product 2', xlabel='category', ylabel='total')
plt.show()

ax = sns.countplot(data = df, x = 'City_Category', hue='Gender')
ax.set(title='Product 2', xlabel='category', ylabel='total')
plt.show()

df.groupby('City_Category').mean()
