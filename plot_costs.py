import sys, os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import numpy as np

def import_data(filename):
    data = pd.read_csv(filename, sep=',', index_col=0)
    data['Percent'] = data['Total']/data['Total'].sum()
    return data

def format_xticks(xtick, pos):
    # use custom ticker formatter to get $
    return '${:,.0f}'.format(xtick)

def plot_data_mpl(data):
    y_pos = np.arange(len(data.index))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_frame_on(False)
    ax.barh(y_pos, data['Total'], align='center', color='grey', lw=0)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(data.index)
    ax.invert_yaxis()

    rects = ax.patches
    labels = ['{:.1f}%'.format(x*100) for x in data['Percent']]
    for rect, label in zip(rects, labels):
        print(rect.get_x(), rect.get_width())
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() + 1000,
                rect.get_y() + height/2,
                label, ha='left', va='center')


    # format x ticks
    x_ticks = [x*1e4 for x in np.arange(0,9,2)]
    ax.set_xticks(x_ticks)
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_tick_params(width=2, length=7, color='grey', labelsize=12)

    formatter = FuncFormatter(format_xticks)
    ax.xaxis.set_major_formatter(formatter)
    for tick in ax.get_xticks():
        print(tick)

    ax.set_xlabel('Total cost in dollars ($)', size=14)

    # format yticks
    ax.yaxis.set_ticks_position('none')
    ax.yaxis.set_tick_params(labelsize=12)

    plt.set_cmap('Greys')
    plt.savefig('2017_cost_plot_mpl.png', bbox_inches='tight')


if __name__ == '__main__':
    hoa_costs = import_data("2017_costs.csv")
    print(hoa_costs)
    plot_data_mpl(hoa_costs)
