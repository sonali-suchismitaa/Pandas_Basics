import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Pandas\email.csv')

#df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Pandas\email.csv', index_col=['Identifier'])

'''print(df.head(2))

#loc - whichever col we set as index_col, that becomes our index value and loc represents location according to that
print(df.loc[2070])
print(df.loc[1,2,3,4])
print(df.loc[5, 'something'])
print(df.loc[5:15], 'something')
print(df.loc[df['Something']<value])
print(df.loc[df['Something']<value], ['To show'])'''


#iloc - actual location, actual index i.e original
print(df.iloc[0])
print(df.iloc[0:3, 0:2]) #row, col