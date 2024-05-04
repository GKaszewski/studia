import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import model_selection
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score
import statsmodels.api as sm

raw_data = pd.read_excel('data/dane_leki.xlsx', index_col=0)
descriptor_columns = raw_data.columns[2:-1]
x = raw_data[descriptor_columns]
y = raw_data.iloc[:, 1]

pca = PCA()
x = pca.fit_transform(x)
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.33, random_state=42)
cv = KFold(n_splits=10, shuffle=True, random_state=1)
linear_reg = LinearRegression().fit(x_train, y_train)
linear_score_train = -1 * cross_val_score(linear_reg, x_train, y_train, cv=cv,
                                          scoring='neg_root_mean_squared_error').mean()
n_components_range = np.arange(1, x.shape[1] + 1)
rmsec_scores = []
n_splits = 10

for n_component in n_components_range:
    pca = PCA(n_components=n_component)
    x_pca = pca.fit_transform(x)
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x_pca, y, test_size=0.33, random_state=42)
    linear_reg = LinearRegression().fit(x_train, y_train)
    linear_score = -1 * cross_val_score(linear_reg, x_train, y_train, cv=cv,
                                        scoring='neg_root_mean_squared_error').mean()
    rmsec_scores.append(linear_score)

plt.plot(n_components_range, rmsec_scores, 'o-')
plt.xlabel('Liczba składowych')
plt.ylabel('RMSEC')
plt.title('RMSEC vs liczba składowych')
plt.grid()
plt.show()

linear_reg.fit(x_train, y_train)
y_train_pred = linear_reg.predict(x_train)
y_test_pred = linear_reg.predict(x_test)

rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
r2_train = r2_score(y_train, y_train_pred)

rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
r2_test = r2_score(y_test, y_test_pred)

print(f'RMSE train: {rmse_train}')
print(f'R2 train: {r2_train}')
print(f'RMSE test: {rmse_test}')
print(f'R2 test: {r2_test}')

best_pc_num = 2
linear_reg_pc = LinearRegression().fit(x_train[:, :best_pc_num], y_train)
pcr_score_train = -1 * cross_val_score(linear_reg_pc, x_train[:, :best_pc_num], y_train, cv=cv,
                                       scoring='neg_root_mean_squared_error').mean()

pred = linear_reg_pc.predict(x_train[:, :best_pc_num])
pred_test = linear_reg_pc.predict(x_test[:, :best_pc_num])

print(f'coef: {linear_reg_pc.coef_}')
print(f'pcr_score_train: {pcr_score_train}')


def get_dataframe_of_scores(set, pca):
    num_pcs = len(pca.components_)
    scores_names = []

    for i in range(num_pcs):
        scores_names.append('PC' + str(i + 1))
    return pd.DataFrame(set, columns=scores_names)


train_df = get_dataframe_of_scores(x_train, pca)
test_df = get_dataframe_of_scores(x_test, pca)

x = sm.add_constant(x_train[:, :best_pc_num])
model1 = sm.OLS(y_train, x).fit()
model2 = sm.OLS(y_train, sm.add_constant(x)).fit()

print(model1.summary())
