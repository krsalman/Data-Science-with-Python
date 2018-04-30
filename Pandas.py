import numpy as np
import pandas as pd
from numpy.random import randn

labels = ['a','b','c']

data = [1,2,3]

list_  = pd.Series(data)
print(list_)

print('***************')

data1 = pd.Series([1,2,3],['python','Reactjs','Django'])

print(data1)
print('***************')

print(data1['Reactjs'])

print('***************')

df = pd.DataFrame({'A':['Salman','Ahmed',np.nan],
                  'B':['Salman',np.nan,np.nan],
                  'C':[1,2,3]})

print(df)

loc_ = df['A']
print('***************')
print(loc_)

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
head = df.head()
print(head)