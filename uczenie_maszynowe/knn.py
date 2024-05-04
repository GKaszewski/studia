from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
import seaborn as sns
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import scale, StandardScaler

data = sns.load_dataset('penguins').dropna()
x = data[['bill_length_mm', 'bill_depth_mm']]
y = data['species']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
kf = KFold(n_splits=10, shuffle=True, random_state=0)
error = []

for i in range(1, 20):
    knn = KNeighborsClassifier(n_neighbors=i, metric='euclidean')
    knn.fit(x_train, y_train)
    pred = knn.predict(x_test)
    error.append(np.mean(pred != y_test))

    # print(f'k: {i}')
    # print(f'accuracy: {knn.score(x_test, y_test)}')

plt.plot(range(1, 20), error, color='red', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')
plt.grid()
plt.show()

report = metrics.classification_report(y_test, pred, output_dict=True)
df = pd.DataFrame(report).transpose()
df['balanced_accuracy'] = 1 - df['recall']

print(df)

plt.figure(figsize=(10, 10))
cm = metrics.confusion_matrix(y_test, pred)
disp = metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=knn.classes_)
disp.plot()
plt.show()

sns.pairplot(data, hue='species', vars=['bill_length_mm', 'bill_depth_mm'])
plt.show()

# zadanie 2

# regression model
numeric_columns = data.select_dtypes(include='number').columns
standarized_data = data.copy()
print(standarized_data.head())
scaler = StandardScaler()
standarized_data[numeric_columns] = scaler.fit_transform(standarized_data[numeric_columns])
print(standarized_data.head())

data = standarized_data

x = data[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']]
y = data['body_mass_g']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
kf = KFold(n_splits=10, shuffle=True, random_state=0)
error = []

for i in range(1, 20):
    knn = KNeighborsRegressor(n_neighbors=i, metric='euclidean')
    knn.fit(x_train, y_train)
    pred = knn.predict(x_test)
    error.append(metrics.mean_squared_error(y_test, pred))

plt.figure(figsize=(10, 10))
sns.scatterplot(data=data, size='body_mass_g', x='bill_length_mm', y='bill_depth_mm', hue='species')
plt.show()

r2 = metrics.r2_score(y_test, pred)
rmse = metrics.mean_squared_error(y_test, pred, squared=False)
q2ex = cross_val_score(knn, x, y, cv=kf, scoring='r2').mean()
rmseex = cross_val_score(knn, x, y, cv=kf, scoring='neg_root_mean_squared_error').mean()

df = pd.DataFrame({'r2': [r2], 'rmse': [rmse], 'q2ex': [q2ex], 'rmseex': [rmseex]})
print(df)
