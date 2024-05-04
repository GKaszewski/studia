import pandas as pd
import scipy
data = pd.read_csv('data/nfloffenseweek3.csv')
filtered_data = data.select_dtypes(exclude=['object'])

min_values = filtered_data.min()
max_values = filtered_data.max()
min_max_ratio = min_values / max_values
max_min = max_values - min_values
mean_values = filtered_data.mean()
center_of_distribution = max_min / 2
standard_deviation = filtered_data.std()
skewness = filtered_data.skew()

print(f'Min values: {min_values}')
print(f'Max values: {max_values}')
print(f'Min/max ratio: {min_max_ratio}')
print(f'Max - min: {max_min}')
print(f'Mean values: {mean_values}')
print(f'Center of distribution: {center_of_distribution}')
print(f'Standard deviation: {standard_deviation}')
print(f'Skewness: {skewness}')