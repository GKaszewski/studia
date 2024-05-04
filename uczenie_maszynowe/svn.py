import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.model_selection as selection
from sklearn import tree
import sklearn.metrics as metrics
import sklearn.preprocessing as preprocessing
from sklearn.preprocessing import scale, StandardScaler

import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

data = pd.read_csv('data/penguins_size.csv')
data.dropna(inplace=True)
print(data.head())

sns.pairplot(data, hue='species')
plt.savefig('wykresik.png', dpi=1000)
plt.show()

data_linear_separable = data[(data['species'] == 'Chinstrap') | (data['species'] == 'Gentoo')]
features_linear_separable = data_linear_separable[['body_mass_g', 'bill_depth_mm']]
labels_linear_separable = data_linear_separable['species']

data_non_linear_separable = data[(data['species'] == 'Chinstrap') | (data['species'] == 'Adelie')]
features_non_linear_separable = data_non_linear_separable[['body_mass_g', 'bill_depth_mm']]
labels_non_linear_separable = data_non_linear_separable['species']

features_train, features_valid, labels_train, labels_valid = train_test_split(
    features_linear_separable, labels_linear_separable, test_size=0.2, random_state=42
)

scaler = StandardScaler()
features_train_scaled = scaler.fit_transform(features_train)
features_valid_scaled = scaler.transform(features_valid)

model_linear_kernel = SVC(kernel='linear')
model_linear_kernel.fit(features_train_scaled, labels_train)

predictions_linear_kernel = model_linear_kernel.predict(features_valid_scaled)
accuracy_linear_kernel = accuracy_score(labels_valid, predictions_linear_kernel)
print(f'Dokładność modelu liniowego: {accuracy_linear_kernel:.2f}')

model_non_linear_linear_kernel = SVC(kernel='linear')
model_non_linear_linear_kernel.fit(features_non_linear_separable, labels_non_linear_separable)

model_non_linear_poly_kernel = SVC(kernel='poly', degree=3)
model_non_linear_poly_kernel.fit(features_non_linear_separable, labels_non_linear_separable)

model_non_linear_rbf_kernel = SVC(kernel='rbf')
model_non_linear_rbf_kernel.fit(features_non_linear_separable, labels_non_linear_separable)

predictions_non_linear_linear_kernel = model_non_linear_linear_kernel.predict(features_valid)
accuracy_non_linear_linear_kernel = accuracy_score(labels_valid, predictions_non_linear_linear_kernel)
print(f'Dokładność modelu z liniowym jądrem dla danych nieliniowych: {accuracy_non_linear_linear_kernel:.2f}')

predictions_non_linear_poly_kernel = model_non_linear_poly_kernel.predict(features_valid)
accuracy_non_linear_poly_kernel = accuracy_score(labels_valid, predictions_non_linear_poly_kernel)
print(f'Dokładność modelu z wielomianowym jądrem dla danych nieliniowych: {accuracy_non_linear_poly_kernel:.2f}')

predictions_non_linear_rbf_kernel = model_non_linear_rbf_kernel.predict(features_valid)
accuracy_non_linear_rbf_kernel = accuracy_score(labels_valid, predictions_non_linear_rbf_kernel)
print(f'Dokładność modelu z jądrem RBF dla danych nieliniowych: {accuracy_non_linear_rbf_kernel:.2f}')

features_scaled = scaler.fit_transform(features_non_linear_separable)
pca = PCA(n_components=2)
features_pca = pca.fit_transform(features_scaled)

model_linear_kernel_pca = SVC(kernel='linear')
model_linear_kernel_pca.fit(features_pca, labels_non_linear_separable)

plt.figure(figsize=(15, 5))

# Wykres dla modelu liniowego
plt.subplot(1, 2, 1)
sns.scatterplot(x=features_pca[:, 0], y=features_pca[:, 1], hue=labels_non_linear_separable, palette='viridis')
sns.scatterplot(x=model_linear_kernel_pca.support_vectors_[:, 0], y=model_linear_kernel_pca.support_vectors_[:, 1],
                marker='o', color='red', label='Support Vectors')
plt.title('Linear Kernel SVM')

plt.show()

# Wykres dla modelu nieliniowych
plt.subplot(1, 2, 2)
sns.scatterplot(x=features_pca[:, 0], y=features_pca[:, 1], hue=labels_non_linear_separable, palette='viridis')
plt.title('Original Data')

plt.show()


# Obliczanie marginesów i wektorów własnych
def plot_svm_decision_margin(model, ax):
    h = .02  # Krok siatki
    x_min, x_max = features_train_scaled[:, 0].min() - 1, features_train_scaled[:, 0].max() + 1
    y_min, y_max = features_train_scaled[:, 1].min() - 1, features_train_scaled[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])

    # Wizualizacja marginesu i wektorów własnych
    Z = Z.reshape(xx.shape)
    ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

    # Zaznaczenie wektorów własnych
    ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=100, facecolors='none',
               edgecolors='k', marker='o', label='Support Vectors')


plt.figure(figsize=(8, 6))

sns.scatterplot(x=features_train_scaled[:, 0], y=features_train_scaled[:, 1], hue=labels_train, palette='viridis')
plot_svm_decision_margin(model_linear_kernel, plt.gca())

plt.title('Linear Kernel SVM - Decision Margin and Support Vectors')
plt.xlabel('Feature 1 (Scaled)')
plt.ylabel('Feature 2 (Scaled)')
plt.legend()
plt.show()

# Wykres dla modelu nieliniowych
plt.subplot(1, 2, 2)
sns.scatterplot(x=features_pca[:, 0], y=features_pca[:, 1], hue=labels_non_linear_separable, palette='viridis')
plt.title('Original Data')

plt.show()
