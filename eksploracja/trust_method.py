import pandas as pd
import numpy as np
import scipy

df = pd.DataFrame({'data': np.random.normal(size=25)})

dropped_value = df.sample(1).index
df = df.drop(dropped_value)
m = df.mean()
s = df.std()
alpha = 0.05

t = scipy.stats.t.ppf(1 - alpha / 2, 24-1)
x_min = (m - t * s)[0]
x_max = (m + t * s)[0]
print(f'x_min = {x_min}, x_max = {x_max}, t = {t}, dropped_value = {dropped_value[0]}')
if x_min < dropped_value < x_max:
    print('do not remove')
else:
    print('remove')