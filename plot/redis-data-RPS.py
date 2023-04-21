import matplotlib.pyplot as plt
import numpy as np
import copy
import csv
from matplotlib.font_manager import FontProperties
import pandas as pd
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter

def plot_line1(_x_ticks, _x_coordinates, _data, _colors, _x_label, _y_label, _line_labels,
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
    plt.ylim(98000,130000)
    # plt.title(title, {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})

    # plot
    plt.plot(_x_coordinates, _data[0], color=_colors[0], marker=_markers[0], label=_line_labels[0], linewidth=3, markersize=8)
    plt.plot(_x_coordinates, _data[1], color=_colors[1], marker=_markers[1], label=_line_labels[1], linewidth=3, markersize=7)
    plt.plot(_x_coordinates, _data[2], color=_colors[2], marker=_markers[2], label=_line_labels[2], linewidth=3, markersize=7)
    plt.grid(linewidth=0.4, axis="y", zorder=0)
    
    # plt.legend(prop=font_prop1, loc=_legend_pos)

def plot_line2(_x_ticks, _x_coordinates, _data, _colors, _x_label, _y_label, _line_labels,
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
    plt.ylim(88000,122000)
    # plt.title(title, {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})

    # plot
    plt.plot(_x_coordinates, _data[0], color=_colors[0], marker=_markers[0], label=_line_labels[0], linewidth=3, markersize=8)
    plt.plot(_x_coordinates, _data[1], color=_colors[1], marker=_markers[1], label=_line_labels[1], linewidth=3, markersize=7)
    plt.plot(_x_coordinates, _data[2], color=_colors[2], marker=_markers[2], label=_line_labels[2], linewidth=3, markersize=7)
    plt.grid(linewidth=0.4, axis="y", zorder=0)
    
    plt.legend(prop=font_prop1, loc=_legend_pos)

def plot_micro_latency(_x_ticks, _x_coordinates, _data_set, _data_get, _colors, _line_labels,
                       _markers, _filename, _legend_pos):
    plt.subplot(121)
    plot_line1(_x_ticks, _x_coordinates, _data_set, _colors, "Data Size(Bytes)", "Redis GET Throughput(rps)",
              _line_labels, _markers,
              _legend_pos)
    plt.subplot(122)
    plot_line2(_x_ticks, _x_coordinates, _data_get, _colors, "Data Size(Bytes)", "Redis SET Throughput(rps)",
              _line_labels, _markers,
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
    x_ticks = ["4", "8", "16", "32", "64", "128", "256", "512", "1K", "2K", "4K"]
    # [orange gold purple green blue]
    colors = ["#F59D56", "#93CDDD", "#7F659F", "#C4D6A0", "#FFD066"]
    markers = ['^', 'D', 'o', 'v', 's']
    labels = ["Bare-Metal", "KVM", "Hummer", "BSD-PIPE", "BSD-TCP"]

    """
    SIZE     4K  8K  16K  32K  64K  128K  256K  512K  1M  2M  4M     
    MEMCPY   --  --  ---  ---  ---  ----  ----  ----  --  --  --
    CP_FILE  --  --  ---  ---  ---  ----  ----  ----  --  --  --
    SCST     --  --  ---  ---  ---  ----  ----  ----  --  --  --
    PIPE     --  --  ---  ---  ---  ----  ----  ----  --  --  --
    TCP      --  --  ---  ---  ---  ----  ----  ----  --  --  --
    """
    _data_get = [
        [111483, 111408, 112360, 110975, 111483, 112133, 112271, 111173, 113186, 112372, 112854],
        [93058, 103767, 107354, 106508, 106815, 105843, 106986, 107875, 105910, 106838, 103929],
        [116850, 117495, 117495, 120525, 118427, 115794, 117027, 117550, 115473, 117925, 112600]
    ]
    _data_set = [
        [115807, 114718, 113033, 114982, 114903, 117261, 116279, 114299, 112752, 108849, 104395],
        [111757, 111086, 107631, 110229, 108015, 112511, 109794, 106803, 108909, 106168, 103295],
        [121907, 123396, 123916, 122519, 125329, 128518, 128304, 122669, 121581, 117938, 113895]
    ]

    plot_micro_latency(x_ticks, x_coordinates, _data_set, _data_get, colors, labels, markers, "./img/redis-data-RPS.pdf",
                       'best')

    