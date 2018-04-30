from __future__ import division
import numpy as np 
import pandas as pd 
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import requests

from StringIO import StringIO


url = "http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv"
source = requests.get(url).text
poll_data = StringIO(source)
poll_df = pd.read_csv(poll_data)
print(poll_df.head())

sns.factorplot('Obama' , data = poll_df , kind ='bar')
plt.show()