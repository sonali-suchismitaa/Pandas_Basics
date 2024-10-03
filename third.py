import pandas as pd

df = pd.read_csv(r"C:\Users\KIIT\Downloads\email.csv")
#print(df)

print(df.columns)
print(df.shape)
print(df.size)
print(df.head(2))  #simply head() will give details of first 5 rows, but if number is provided it will provide info of that many rows
print(df.tail())

print(df.describe())
print(df.info())
