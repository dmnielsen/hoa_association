import sys, os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import numpy as np
import argparse

def import_data(filename):
    data = pd.read_csv(filename, sep=',', index_col=0)
    data['Percent'] = data['Total']/data['Total'].sum()
    return data

def format_xticks(xtick, pos):
    # use custom ticker formatter to get $
    return '${:,.0f}'.format(xtick)

def plot_data(data, out_fn):
    y_pos = np.arange(len(data.index))

    fig = plt.figure(figsize=(8.5,4.75))
    ax = fig.add_subplot(111)
    ax.set_frame_on(False)

    # plot figure
    ax.barh(y_pos, data['Total'], align='center', color='grey', lw=0)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(data.index)
    ax.invert_yaxis()

    # plot percentage labels
    rects = ax.patches
    labels = ['{:.1f}%'.format(x*100) for x in data['Percent']]
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() + 1000,
                rect.get_y() + height/2,
                label, ha='left', va='center')


    # format x ticks
    x_ticks = [x*1e4 for x in np.arange(0,9,2)]
    ax.set_xticks(x_ticks)
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_tick_params(width=2, length=7, color='lightgrey', labelsize=12)

    formatter = FuncFormatter(format_xticks)
    ax.xaxis.set_major_formatter(formatter)

    ax.set_xlabel('Total cost in dollars ($)', size=14)

    # format yticks
    ax.yaxis.set_ticks_position('none')
    ax.yaxis.set_tick_params(labelsize=12)

    plt.savefig(out_fn, format='pdf', bbox_inches='tight')

def define_out_file():
    if args.out_file is None:
        args.out_file = args.in_file[:-4]+'_plot.pdf'


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="CSV file of expenses to plot")
    parser.add_argument("-o", "--out_file", help="output filename for image, \
                        default 'in_file_plot.pdf'")
    args = parser.parse_args()
    define_out_file()

    hoa_costs = import_data(args.in_file)
    plot_data(hoa_costs, args.out_file)
