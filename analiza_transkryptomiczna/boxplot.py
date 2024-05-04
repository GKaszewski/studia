import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('data/Dane_BoxPlot.xlsx')
features = data.iloc[:, 1:]

plt.figure(figsize=(10, 6))
sns.boxplot(data=features, orient='h', palette='Set2')
sns.stripplot(data=features, orient='h', color='black', alpha=0.5)
plt.title('Box plot of the data')
plt.show()

