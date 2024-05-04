import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_volcano_plot(name, data, annonate=False):
    x = data['LogFC']
    y = -np.log10(data['P-value'])
    y_cutoff = 1.3
    x_cutoff = 0.2

    valid_genes = data[(data['LogFC'] > x_cutoff) | (data['LogFC'] < -x_cutoff) & (data['P-value'] < y_cutoff)]
    print(valid_genes)
    valid_genes.to_excel(name + '_valid_genes.xlsx')

    # display volcano plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.5)
    plt.axvline(x=x_cutoff, color='g', linestyle='--', label=f'LogFC = {x_cutoff}')
    plt.axvline(x=-x_cutoff, color='g', linestyle='--')
    plt.axhline(y=y_cutoff, color='g', linestyle='--', label=f'P-value = {y_cutoff}')
    plt.axhline(y=-y_cutoff, color='g', linestyle='--')
    plt.xlabel('LogFC')
    plt.ylabel('-log10(P-value)')
    plt.title('Volcano plot for ' + name)
    if annonate:
        for i in range(len(data)):
            plt.annotate(data['Gene_ID'][i], (x[i], y[i]))
    plt.grid(True)
    plt.show()


def get_venn_diagram(data1, data2, data3):
    from matplotlib_venn import venn3
    from matplotlib import pyplot as plt

    set1 = set(data1['Gene_ID'])
    set2 = set(data2['Gene_ID'])
    set3 = set(data3['Gene_ID'])

    venn3([set1, set2, set3],
          ('Acute Phase Response Signaling', 'Agranulocyte Adhesion and Diaped', 'Granulocyte Adhesion and Diaped'))
    plt.show()


data_1 = pd.read_excel('data/Tabela-2.xlsx', sheet_name='Acute Phase Response Signaling')
get_volcano_plot('Acute Phase Response Signaling', data_1)
data_2 = pd.read_excel('data/Tabela-2.xlsx', sheet_name='Agranulocyte Adhesion and Diape')
get_volcano_plot('Agranulocyte Adhesion and Diape', data_2)
data_3 = pd.read_excel('data/Tabela-2.xlsx', sheet_name='Granulocyte Adhesion and Diaped')
get_volcano_plot('Granulocyte Adhesion and Diaped', data_3, annonate=True)

get_venn_diagram(data_1, data_2, data_3)
