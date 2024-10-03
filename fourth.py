#handling missing values 
import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Pandas\Diabetes Missing Data.csv')

print(df)
print(df.head())
print(df.isnull().sum())  #sum of corresponding col null values
print(df.isnull().sum().sum()) #total number of null values in csv

#drop rows
print(df.shape)
df2 = df.dropna() #default axis = 0 (means rows), deletes all null valued rows
print(df2.shape)

#drop cols
df3 = df.dropna(axis=1)  #drop cols if axis = 1
print(df3.shape)

#if all the values of the row are null
print(df.dropna(how = 'all'))

print(df.dropna(inplace=True))  #makes sure there are no null values 
print(df.shape)