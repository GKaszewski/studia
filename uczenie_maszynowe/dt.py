import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.model_selection as selection
from sklearn import tree
import sklearn.metrics as metrics
import sklearn.preprocessing as preprocessing
from sklearn.metrics import confusion_matrix, classification_report, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

data = pd.read_excel('data/dane_nano1.xlsx')
data = data[:10]
descriptor_column_names = ['Size', 'SSA']
descriptors = data[descriptor_column_names]
y = data['Protein carbonylation (A-1/I-0)']

train_data, test_data, train_target, test_target = selection.train_test_split(descriptors, y, test_size=0.3,
                                                                              random_state=0)

model = tree.DecisionTreeClassifier(random_state=0)
model.fit(train_data, train_target)
predictions = model.predict(test_data)

tree.plot_tree(model)
plt.show()

tn, fp, fn, tp = confusion_matrix(test_target, predictions).ravel()
sns.heatmap(confusion_matrix(test_target, predictions), annot=True)
plt.show()
senstivity = tp / (tp + fn)
specificity = tn / (tn + fp)
precision = tp / (tp + fp)
f1 = 2 * (precision * senstivity) / (precision + senstivity)
balanced_accuracy = (senstivity + specificity) / 2
balanced_error = 1 - balanced_accuracy
df = pd.DataFrame(
    {'sensitivity': [senstivity], 'specificity': [specificity], 'precision': [precision], 'f1': [f1],
     'balanced_accuracy': [balanced_accuracy], 'balanced_error': [balanced_error]})
print(df)
df.to_excel('wyniki.xlsx', index=False)

data_to_predict = pd.read_excel('data/dane_nano1.xlsx')
data_to_predict = data_to_predict[10:]
data_to_predict = data_to_predict[descriptor_column_names]
predictions = model.predict(data_to_predict)
print(predictions)
data_to_predict['predictions'] = predictions
data_to_predict.to_excel('data/dane_nano1_nowe.xlsx', index=False)

# zadanie 2

data = pd.read_excel('data/dane_nano2.xlsx')
data = data[:17]
# Przygotowanie danych
descriptors = data[['Size', 'SSA', 'SHELPRES', 'LUMO_C']]
y = data[['Measured NOEAC [mg/m3]']]
descriptors = preprocessing.scale(descriptors)
y = preprocessing.scale(y)
# Podział danych na zestawy uczące i testowe
train_data, test_data, train_target, test_target = train_test_split(
    descriptors, y, test_size=0.3, random_state=0)

# Budowanie modelu drzewa regresyjnego
regressor = DecisionTreeRegressor()
regressor.fit(train_data, train_target)

# Predykcja na danych testowych
predictions = regressor.predict(test_data)
print('predictions:', predictions)

# Obliczanie RMSE (Root Mean Squared Error)
rmse = metrics.mean_squared_error(test_target, predictions, squared=False)
q2ex = metrics.r2_score(test_target, predictions)
print(f'RMSE: {rmse}')
print(f'Q2Ex: {q2ex}')

# Predykcja na danych do predykcji
data_to_predict = pd.read_excel('data/dane_nano2.xlsx')
data_to_predict = data_to_predict[17:]
descriptors_pred = data_to_predict[['Size', 'SSA', 'SHELPRES', 'LUMO_C']]
descriptors_pred = preprocessing.scale(descriptors_pred)
predictions_new = regressor.predict(descriptors_pred)
print('predictions:', predictions_new)
data_to_predict['predictions'] = predictions_new
data_to_predict.to_excel('data/dane_nano2_nowe.xlsx', index=False)
