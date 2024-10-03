import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Pandas\Diabetes Missing Data.csv')


#Group By
branch_group = df.groupby(by = 'Age')
print(branch_group)
print(branch_group.groups)

for group, data_frame in branch_group:
    print(group)
    print(data_frame)


#Merge
df1 = pd.DataFrame({'Roll No':[1,2,3,4,5], 'Phy':[98,99,97, 91, 92]})
df2 = pd.DataFrame({'Roll No': [1,2,3,4,5], 'Chem':[12,13,14,15,16]})
#print(pd.merge(df1, df2, on='Roll No')) #by default intersecting col is chosen

df3 = pd.DataFrame({'Roll No':[1,2,3,4,5], 'Phy':[98,99,97, 91, 92]})
df4 = pd.DataFrame({'Roll No': [1,2,3,6,7], 'Chem':[12,13,14,15,16]})
print(pd.merge(df3, df4))
print(pd.merge(df3,df4, how = 'right'))  #only df4 col shall be printed
print(pd.merge(df3, df4, how = 'outer'))  #print all roll 