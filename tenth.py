import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Pandas\engg.csv')
print(pd.pivot_table(df, index = 'Branch'))
print(pd.pivot_table(df, index = 'Branch', aggfunc = 'sum'))
print(pd.pivot_table(df, index = 'Branch', aggfunc = 'count'))
print(pd.pivot_table(df, index = 'Branch', aggfunc = 'max'))
print(pd.pivot_table(df, index = 'Branch', columns = 'Section'))