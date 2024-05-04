import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn.linear_model as lm
import statsmodels.api as sm
import sklearn.model_selection as ms
from sklearn import metrics

raw_data = pd.read_excel('data/dane_leki.xlsx')
numeric_columns = raw_data.select_dtypes(include='number').columns
descriptor_columns = raw_data.columns[3:-1]
print(f'descriptor_columns: {descriptor_columns}')
# check correlation between variables
corr = raw_data[descriptor_columns].corr()
sns.heatmap(corr, annot=True)
plt.show()

train_data = raw_data[raw_data['Zbiór'] == 't'].copy()
test_data = raw_data[raw_data['Zbiór'] == 'w'].copy()

# create model
model = lm.LinearRegression()
model.fit(train_data[descriptor_columns], train_data['logK HSA'])
print(f'intercept: {model.intercept_}')
print(f'coefficients: {model.coef_}')

# predict
train_data['logK HSA predicted'] = model.predict(train_data[descriptor_columns])
test_data['logK HSA predicted'] = model.predict(test_data[descriptor_columns])

r2 = model.score(test_data[descriptor_columns], test_data['logK HSA'])
rmsec = metrics.mean_squared_error(test_data['logK HSA'], test_data['logK HSA predicted'], squared=False)
rmse_cvloo = ms.cross_val_score(model, raw_data[descriptor_columns], raw_data['logK HSA'], cv=ms.LeaveOneOut(),
                                scoring='neg_root_mean_squared_error').mean()
q2ex = 1 - (rmsec / rmse_cvloo)
rmse_ex = rmsec * np.sqrt(q2ex)
f = (q2ex / (1 - q2ex)) * ((raw_data.shape[0] - 1 - 1) / (raw_data.shape[0] - raw_data.shape[1] - 1))

print(f'r2: {r2}')
print(f'rmsec: {rmsec}')
print(f'rmse_cvloo: {rmse_cvloo}')
print(f'q2ex: {q2ex}')
print(f'rmse_ex: {rmse_ex}')
print(f'f: {f}')

# plot predicted vs real
plt.scatter(train_data['logK HSA'], train_data['logK HSA predicted'], label='train')
plt.scatter(test_data['logK HSA'], test_data['logK HSA predicted'], label='test')
plt.plot([train_data['logK HSA'].min(), train_data['logK HSA'].max()],
         [train_data['logK HSA'].min(), train_data['logK HSA'].max()], 'k--', lw=4)
plt.xlabel('logK HSA')
plt.ylabel('logK HSA predicted')
plt.legend()
plt.text(0.05, 0.80, f'R2: {r2}', transform=plt.gca().transAxes)
plt.show()

