import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import numpy as np

data = pd.read_excel('data/Dane_Eggplants_Percent.xlsx')
features = data.columns[1:]
x = data.loc[:, features].values
x = StandardScaler().fit_transform(x)

covariance_matrix = np.cov(x.T)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
eigenvalues = sorted(eigenvalues, reverse=True)

plt.figure(figsize=(10, 6))
sing_vals = np.arange(len(eigenvalues)) + 1
plt.plot(sing_vals, eigenvalues, 'ro-', linewidth=2)
plt.axhline(y=1, color='b', linestyle='--')
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Eigenvalue')
plt.grid(True)
plt.show()

pca = PCA(n_components=5)
principal_components = pca.fit_transform(x)
principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5'])


def plot_pca(pca_matrix, first_var, second_var):
    plt.figure(figsize=(10, 6))
    plt.scatter(pca_matrix.iloc[:, first_var], pca_matrix.iloc[:, second_var], alpha=0.5)
    plt.title('PCA')
    plt.xlabel('PC' + str(first_var + 1))
    plt.ylabel('PC' + str(second_var + 1))
    plt.grid(True)
    plt.show()


for i in range(5):
    for j in range(i + 1, 5):
        plot_pca(principal_df, i, j)
