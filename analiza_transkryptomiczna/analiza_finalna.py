import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import numpy as np

data = pd.read_excel('data/Metabolomika_Finalny2024.xlsx')
mice = data.loc[
    data['Group'].isin(['F_Mutacja2', 'F_Mutacja1', 'F_Kontrola', 'M_Mutacja2', 'M_Mutacja1', 'M_Kontrola'])]
blank = data.loc[data['Group'] == 'Blank']
qc = data.loc[data['Group'] == 'QC']

features = mice.iloc[:, 2:]

mice_mean = features.mean()
forty_percentile_of_avg = mice_mean * 0.4

blank_mean = blank.iloc[:, 2:].mean()

features_to_drop = blank_mean[blank_mean > forty_percentile_of_avg].index
mice_filtered = features.drop(columns=features_to_drop)

print(f'Mice Mean: {mice_mean}')
print(f'40% of mice mean: {forty_percentile_of_avg}')

print(f'Blank Mean: {blank_mean}')

print(f"Original number of features: {features.shape[1]}")
print(f"Number of features after dropping: {mice_filtered.shape[1]}")

# mice_filtered.to_excel('mice_filtered.xlsx', index=False)
data_filtered = pd.concat([mice[['Id', 'Group']], mice_filtered], axis=1)
print(f"Number of features after dropping: {data_filtered.shape[1]}")
# data_filtered.to_excel('data_filtered.xlsx', index=False)

scaler = StandardScaler()
x = mice_filtered.values
x = scaler.fit_transform(x)

covariance_matrix = np.cov(x.T)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
eigenvalues = sorted(eigenvalues, reverse=True)

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
final_df = pd.concat([principal_df, mice[['Group']], mice[['Id']]], axis=1)


def plot_pca(pca_matrix, first_var, second_var, qc_blank_df):
    # plt.scatter(pca_matrix.iloc[:, first_var], pca_matrix.iloc[:, second_var], alpha=0.5)
    sns.scatterplot(x=f'PC{first_var + 1}', y=f"PC{second_var + 1}", hue="Group", data=pca_matrix,
                    palette="Set2", s=100, alpha=0.7)
    sns.scatterplot(x=f'PC{first_var + 1}', y=f"PC{second_var + 1}", data=qc_blank_df, hue='Group', s=100, alpha=0.7,
                    palette='Set1')
    plt.title('PCA')
    plt.xlabel('PC' + str(first_var + 1))
    plt.ylabel('PC' + str(second_var + 1))
    plt.grid(True)
    plt.show()


blank_qc = data.loc[data['Group'].isin(['Blank', 'QC'])]
qc_blank_df = pd.merge(blank_qc, principal_df, left_on='Id', right_index=True, how='inner')

for i in range(5):
    for j in range(i + 1, 5):
        plot_pca(final_df, i, j, qc_blank_df)

# plot female and male species
data_plot = pd.concat([principal_df, mice[['Group']]], axis=1)
data_plot['Group'] = data_plot['Group'].apply(lambda x: x[0])
sns.pairplot(data_plot, hue='Group', palette='Set2')
plt.show()

# plot by mutation
data_plot = pd.concat([principal_df, mice[['Group']]], axis=1)
data_plot['Group'] = data_plot['Group'].apply(lambda x: x.split('_')[1])
# select only mutation
data_plot = data_plot.loc[data_plot['Group'].str.contains('Mutacja')]
sns.pairplot(data_plot, hue='Group', palette='Set1')
plt.show()

# plot mutation vs control
data_plot = pd.concat([principal_df, mice[['Group']]], axis=1)
data_plot['Group'] = data_plot['Group'].apply(lambda x: x.split('_')[1])
data_plot['Group'] = data_plot['Group'].apply(lambda x: 'Control' if x == 'Kontrola' else 'Mutation')
sns.pairplot(data_plot, hue='Group', palette='Set3')
plt.show()
