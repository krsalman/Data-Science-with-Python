import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.barplot(x='sex',y='total_bill',data=tips)
plt.show()