import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Pandas\Diabetes Missing Data.csv')
print(df.head())
df = df.replace(to_replace=21, value=20)  #can also be written as df.replace(21, 20)
print(df.head())


#df = df.replace(to_replace = [1,2,3,4], value = 'A)
#df = df.replace(to_replace = [1,2,3], value = ['A', 'B', 'C'])
#df = df[Particular col].replace(to_replace = [1,2,3], value = ['A', 'B', 'C'])

#df = df.replace('[A-Za-z]', 0, regex = True)
#df = df.replace(to_replace=28, 'ffill/bfill)