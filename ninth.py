#append() 
import pandas as pd

df1 = pd.DataFrame({'Roll No':[1,2,3,4,5], 'Phy':[98,99,97, 91, 92]})
df2 = pd.DataFrame({'Roll No': [6,7,8,9,10], 'Phy':[12,13,14,15,16]})
print(df1._append(df2))  #indexing starts again when one df is covered
print(df1._append(df2, ignore_index = True))   #indexes are continued
print(df1._append(df2, ignore_index = True, sort = True))  #sorts col names based

df1 = pd.DataFrame({'Roll No':[1,2,3,4,5], 'Phy':[98,99,97, 91, 92]})
df2 = pd.DataFrame({'Roll No': [1,2,3,4,5], 'Chem':[12,13,14,15,16]})
print(df1._append(df2, ignore_index = True))