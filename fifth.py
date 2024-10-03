import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Pandas\Diabetes Missing Data.csv')
print(df.fillna(0)) #fill null values in 0
df.fillna(2) #fills nullvalues with 2

df.fillna({'Pregnant':'none', 'Age':18})  #for null values present in class before : the corresponding after : values will be placed

df.fillna(method = 'ffill') #ffill = forward fill, uses just the previous row value 
df.fillna(method = 'ffill', axis = 1) #it will use the data of previous col

#if method = bfill, it will use the next val (if axis = 0, next row) (if axis = 1, next col)

print(df['Age'].fillna(value = df['Age'].mean()))  #replaces null with mean of the col
