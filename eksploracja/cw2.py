import glob
import os

import pandas as pd
from pandas import DataFrame


def read_all_csvs():
    return pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "data/*.csv"))))


def read_one_csv(path):
    return pd.read_csv(path)


def count_miami_dolphins(df):
    return df[df['team'] == 'Miami Dolphins'].count()[0]


def get_arizona_cardinals_index(df):
    return df[df['team'] == 'Arizona Cardinals'].index


def get_reduced_dataset(df):
    return df.drop(df.index[-3:-1])


def switch_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    return df[col_list]


def switch_rows(df, row1, row2):
    df.iloc[row1], df.iloc[row2] = df.iloc[row2].copy(), df.iloc[row1].copy()
    return df


def save_df_to_csv(df, path):
    df.to_csv(path, index=False)


def save_df_to_xlsx(df, path):
    df.to_excel(path, index=False)


def save_column_names_to_txt(df, path):
    with open(path, 'w') as f:
        f.write('\n'.join(df.columns))


def save_first_n_rows(df: DataFrame, n):
    rows = df.head(n)
    save_df_to_csv(rows, f'data/first_{n}_rows.csv')


def save_last_n_rows(df: DataFrame, n):
    rows = df.tail(n)
    save_df_to_csv(rows, f'data/last_{n}_rows.csv')


def save_combined_first_and_last_n_rows(df: DataFrame, n1, n2):
    rows = pd.concat([df.head(n1), df.tail(n2)])
    save_df_to_csv(rows, f'data/first_and_last_{n1}-{n2}_rows.csv')


def get_n_row_in_j_column(df: DataFrame, n, j):
    return df.iloc[n, j]


def remove_column(df: DataFrame, col_index):
    return df.pop(df.columns[col_index])


def add_column_to_df(df: DataFrame, col):
    return pd.concat([df, col], axis=1)


dataset = read_one_csv('data/nfloffenseweek3.csv')
miami_count = count_miami_dolphins(dataset)
arizona_cardinals_index = get_arizona_cardinals_index(dataset)
print(f'Miami Dolphins count: {miami_count}')
print(f'Arizona Cardinals index: {arizona_cardinals_index}')
reduced_dataset = get_reduced_dataset(dataset)
switched_columns = switch_columns(dataset, dataset.iloc[:, 0].name, dataset.iloc[:, 2].name)
switched_rows = switch_rows(switched_columns, 0, len(dataset.values) - 1)
print(switched_rows)
save_df_to_csv(switched_rows, 'data/switched_rows.csv')
save_df_to_xlsx(switched_rows, 'data/switched_rows.xlsx')
save_column_names_to_txt(switched_rows, 'data/column_names.txt')

save_combined_first_and_last_n_rows(dataset, 5, 7)
obj = get_n_row_in_j_column(dataset, 4, 2)
print(f'Object in 5th row and 3nd column: {obj}')
removed_column = remove_column(dataset, 5)
new_dataset = add_column_to_df(dataset, removed_column)
print(new_dataset)
