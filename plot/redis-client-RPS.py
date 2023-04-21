import matplotlib.pyplot as plt
import numpy as np
import copy
import csv
from matplotlib.font_manager import FontProperties
import pandas as pd
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter

def plot_line(_x_ticks, _x_coordinates, _data, _colors, _x_label, _y_label, _line_labels,
              _markers, _legend_pos):
    types = len(_data)
    # Set ticks
    font_prop1 = FontProperties(family='Times New Roman', weight='normal', size=20)
    font_prop2 = FontProperties(family='Times New Roman', weight='normal', size=20)
    plt.xticks(_x_coordinates, _x_ticks)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
    xtick_labels = plt.gca().get_xticklabels()
    ytick_labels = plt.gca().get_yticklabels()
    [xtick_label.set_fontproperties(font_prop1) for xtick_label in xtick_labels]
    [ytick_label.set_fontproperties(font_prop2) for ytick_label in ytick_labels]

    # Set x, y labels
    plt.xlabel(_x_label, {'family': 'Times New Roman', 'weight': 'bold', 'size': 20})
    plt.ylabel(_y_label, {'family': 'Times New Roman', 'weight': 'bold', 'size': 20})
    plt.ylim(68000,120000)
    # plt.title(title, {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})

    # plot
    plt.plot(_x_coordinates, _data[0], color=_colors[0], marker=_markers[0], label=_line_labels[0], linewidth=3, markersize=8)
    plt.plot(_x_coordinates, _data[1], color=_colors[1], marker=_markers[1], label=_line_labels[1], linewidth=3, markersize=7)
    plt.plot(_x_coordinates, _data[2], color=_colors[2], marker=_markers[2], label=_line_labels[2], linewidth=3, markersize=7)
    plt.grid(linewidth=0.4, axis="y", zorder=0)
    
    plt.legend(prop=font_prop1, loc=_legend_pos)

def plot_client_rps(_x_ticks, _x_coordinates, _data_set, _data_get, _colors, _line_labels,
                    _markers, _filename, _legend_pos):
    plt.subplot(121)
    plot_line(_x_ticks, _x_coordinates, _data_set, _colors, "Client Number", "Redis GET Throughput(rps)", _line_labels,
              _markers,
              _legend_pos)
    plt.subplot(122)
    plot_line(_x_ticks, _x_coordinates, _data_get, _colors, "Client Number", "Redis SET Throughput(rps)", _line_labels,
              _markers,
              _legend_pos)
    plt.savefig(_filename, bbox_inches='tight')
    plt.show()
    print("Save send-recv.pdf")
    plt.clf()

if __name__ == "__main__":
    plt.rc('font', family='Times New Roman', weight='normal', size=15)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['figure.figsize'] = (16.0, 5.0)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 100
    plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
    # draw recv side figure
    x_coordinates = np.array(range(1, 12, 1))
    x_ticks = ["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096"]
    # [orange gold purple green blue]
    colors = ["#F59D56", "#93CDDD", "#7F659F", "#C4D6A0", "#FFD066"]
    markers = ['^', 'D', 'o', 'v', 's']
    labels = ["Bare-Metal", "KVM", "Hummer", "BSD-PIPE", "BSD-TCP"]

    _client_get = [
        [100321, 96637, 89429, 76080, 71592, 72119, 76242, 76894, 75460, 74272],
        [94958, 90214, 85763, 77706, 73223, 72062, 75375, 74532, 71917, 72093],
        [113007, 108213, 93853, 77815, 72469, 73470, 77149, 82008, 77244, 70037]
    ]
    _client_set = [
        [102796, 96543, 90244, 74794, 70284, 71823, 75706, 75233, 74161, 73314],
        [95575, 89429, 84502, 76587, 71644, 71906, 74901, 73470, 72233, 71855],
        [117014, 112473, 97694, 75580, 72611, 73223, 75272, 78425, 70691, 69589]
    ]
    x_coordinates = np.array(range(1, 11, 1))
    x_ticks = ["1K", "2K", "3K", "4K", "5K", "6K", "7K", "8K", "9K", "10K"]
    plot_client_rps(x_ticks, x_coordinates, _client_set, _client_get, colors, labels, markers, "./img/redis-client-RPS.pdf",
                    'best')

    