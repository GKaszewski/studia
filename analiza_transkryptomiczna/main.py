import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = pd.read_excel('data/Tabela-1.xlsx')

features = data.columns[5:]
x = data.loc[:, features].values
x = StandardScaler().fit_transform(x)

# PCA

pca = PCA(n_components=3)
principal_components = pca.fit_transform(x)
principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2', 'PC3'])

final_df = pd.concat([principal_df, data[['Chemical', 'SEX (M/F)']]], axis=1)

plt.figure(figsize=(20, 10))
sns.scatterplot(x="PC1", y="PC2", hue="Chemical", style="SEX (M/F)", data=final_df, palette="Set2", s=100, alpha=0.7)
plt.title('PCA of Gene Expression Data by Chemical and Gender')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Chemical/Gender', bbox_to_anchor=(1, 1), loc='upper left')
plt.grid(True)
plt.show()

plt.figure(figsize=(20, 10))
sns.scatterplot(x="PC1", y="PC3", hue="Chemical", style="SEX (M/F)", data=final_df, palette="Set2", s=100, alpha=0.7)
plt.title('PCA of Gene Expression Data by Chemical and Gender')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 3')
plt.legend(title='Chemical/Gender', bbox_to_anchor=(1, 1), loc='upper left')
plt.grid(True)
plt.show()

plt.figure(figsize=(20, 10))
sns.scatterplot(x="PC2", y="PC3", hue="Chemical", style="SEX (M/F)", data=final_df, palette="Set2", s=100, alpha=0.7)
plt.title('PCA of Gene Expression Data by Chemical and Gender')
plt.xlabel('Principal Component 2')
plt.ylabel('Principal Component 3')
plt.legend(title='Chemical/Gender', bbox_to_anchor=(1, 1), loc='upper left')
plt.grid(True)
plt.show()

# Get 10 most important features for each PC (sort by absolute value)
# PC1
most_important_features_pc1 = pd.DataFrame(pca.components_[0] * np.sqrt(pca.explained_variance_[0]), index=features, columns=['PC1'])
most_important_features_pc1['abs'] = most_important_features_pc1['PC1'].abs()
most_important_features_pc1 = most_important_features_pc1[most_important_features_pc1['abs'] > 0.7].sort_values(by='abs', ascending=False).drop(columns='abs')
print(most_important_features_pc1.head(10))
most_important_features_pc1.to_excel('most_important_features_pc1.xlsx')

# PC2
most_important_features_pc2 = pd.DataFrame(pca.components_[1] * np.sqrt(pca.explained_variance_[1]), index=features, columns=['PC2'])
most_important_features_pc2['abs'] = most_important_features_pc2['PC2'].abs()
most_important_features_pc2 = most_important_features_pc2[most_important_features_pc2['abs'] > 0.7].sort_values(by='abs', ascending=False).drop(columns='abs')
print(most_important_features_pc2.head(10))
most_important_features_pc2.to_excel('most_important_features_pc2.xlsx')

# select data where chemical is 'Pb' and 'Hg'
data = data[(data['Chemical'] == 'Pb') | (data['Chemical'] == 'Hg')]
x = data.loc[:, features].values
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(x)
principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

