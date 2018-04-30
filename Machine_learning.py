import numpy as np 
import pandas as pd 

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('USA_Housing.csv')
data = df.head()
print(data)
print(df.describe())


