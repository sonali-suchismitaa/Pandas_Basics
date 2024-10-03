import pandas as pd
#print(pd.__version__)

lst = [1,2,3,4,5,6]
print(lst)

series = pd.Series(lst)   #shows indexes and values
print(series)
print(type(series))

empty = pd.Series([])
print(empty)

a = pd.Series(['p', 'q', 'r', 's', 't'], index = [10,11,12,18,19])
print(a)

b = pd.Series(['a', 'b', 'c', 'd', 'e'], index = [1,2,3,4,5], name = 'Alphabets')
print(b)

scalar_series = pd.Series(0.5)
print(scalar_series)

scalar_series = pd.Series(0.5, index = ([1,2,3]), name = 'Floats')
print(scalar_series)

dict_series = pd.Series({'p':1, 'q':2}) #before : are the indexes, after : are the values
print(dict_series)

print(dict_series[0:2])
print(max(dict_series))

dict_series = pd.Series({'p':[1,2,3], 'q':[4,5,6], 'r':[7,8,9]}, name = 'Tups')
print(dict_series)