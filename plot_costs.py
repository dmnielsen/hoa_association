import sys, os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
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

def format_xticks(xtick, pos):
    # use custom ticker formatter to get $
    return '${:,.0f}'.format(xtick)

def plot_data_mpl(data):
    y_pos = np.arange(len(data.index))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.barh(y_pos, data['Total'], align='center')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(data.index)
    ax.invert_yaxis()

    formatter = FuncFormatter(format_xticks)
    ax.xaxis.set_major_formatter(formatter)

    plt.savefig('2017_cost_plot_mpl.png', bbox_inches='tight')


if __name__ == '__main__':
    hoa_costs = import_data("2017_costs.csv")
    print(hoa_costs)
    plot_data_mpl(hoa_costs)
