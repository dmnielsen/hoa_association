import sys, os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def import_data(filename):
    data = pd.read_csv(filename, sep=',', index_col=0)
    return data

def plot_data_pandas(data):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    data.plot(kind='barh', legend=False)
    print(['${:,}'.format(x, grouping=True) for x in data['Total']])
    xticks = ax.get_xticks(); print(xticks)
    ax.set_xticklabels(['${:,}'.format(x, grouping=True) for x in data['Total']])


    ax.invert_yaxis()
    plt.savefig('2017_cost_plot.png')


if __name__ == '__main__':
    hoa_costs = import_data("2017_costs.csv")
    print(hoa_costs)
    plot_data(hoa_costs)
