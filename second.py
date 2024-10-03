import pandas as pd
'''
df = pd.DataFrame()
print(df)'''

lst = ([1,2,3,4,5],[6,7,8,9,10])  #5 cols, 2 rows
df = pd.DataFrame(lst)
print(df) 

#for dict

a = [{'a':5, 'b': 6, 'c':7, 'd':8}, {'a':5, 'b': 6, 'c':7, 'd':8}] #dict keys (in this case Letters) represent col names
df = pd.DataFrame(a)
print(df)

college = {'Roll Number':pd.Series([22053540, 22053621, 22053640, 22054162]),
           'Name': pd.Series(['Saswatt', 'Sanchita', 'Sonali', 'Rajkumar']),
           'CGPA':([7.53, 8.64, 9.13, 7.57])}
df = pd.DataFrame(college)
print(df)

#df = pd.read_csv(r'C:\Users\KIIT\Desktop\Machine Learning\Python\Pandas\CSE_29_Internal_Lab_Marks_30.csv', encoding='latin1')
#print(df)