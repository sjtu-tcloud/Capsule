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
    # plt.ylim(98000,130000)
    # plt.title(title, {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})

    # plot
    plt.plot(_x_coordinates, _data[0], color=_colors[0], marker=_markers[0], label=_line_labels[0], linewidth=3, markersize=8)
    plt.plot(_x_coordinates, _data[1], color=_colors[1], marker=_markers[1], label=_line_labels[1], linewidth=3, markersize=7)
    plt.plot(_x_coordinates, _data[2], color=_colors[2], marker=_markers[2], label=_line_labels[2], linewidth=3, markersize=7)
    plt.grid(linewidth=0.4, axis="y", zorder=0)
    
    plt.legend(prop=font_prop1, loc=_legend_pos)

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
    # plt.ylim(88000,122000)
    # plt.title(title, {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})

    # plot
    plt.plot(_x_coordinates, _data[0], color=_colors[0], marker=_markers[0], label=_line_labels[0], linewidth=3, markersize=8)
    plt.plot(_x_coordinates, _data[1], color=_colors[1], marker=_markers[1], label=_line_labels[1], linewidth=3, markersize=7)
    plt.plot(_x_coordinates, _data[2], color=_colors[2], marker=_markers[2], label=_line_labels[2], linewidth=3, markersize=7)
    plt.grid(linewidth=0.4, axis="y", zorder=0)
    
    # plt.legend(prop=font_prop1, loc=_legend_pos)

def plot_line3(_x_ticks, _x_coordinates, _data, _colors, _x_label, _y_label, _line_labels,
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
    # plt.ylim(88000,122000)
    # plt.title('', {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})

    # plot
    plt.plot(_x_coordinates, _data[0], color=_colors[0], marker=_markers[0], label=_line_labels[0], linewidth=3, markersize=8)
    plt.plot(_x_coordinates, _data[1], color=_colors[1], marker=_markers[1], label=_line_labels[1], linewidth=3, markersize=7)
    plt.plot(_x_coordinates, _data[2], color=_colors[2], marker=_markers[2], label=_line_labels[2], linewidth=3, markersize=7)
    plt.grid(linewidth=0.4, axis="y", zorder=0)
    
    # plt.legend(prop=font_prop1, loc=_legend_pos)

def plot_line4(_x_ticks, _x_coordinates, _data, _colors, _x_label, _y_label, _line_labels,
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
    # plt.ylim(88000,122000)
    # plt.title(" ", {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})

    # plot
    plt.plot(_x_coordinates, _data[0], color=_colors[0], marker=_markers[0], label=_line_labels[0], linewidth=3, markersize=8)
    plt.plot(_x_coordinates, _data[1], color=_colors[1], marker=_markers[1], label=_line_labels[1], linewidth=3, markersize=7)
    plt.plot(_x_coordinates, _data[2], color=_colors[2], marker=_markers[2], label=_line_labels[2], linewidth=3, markersize=7)
    plt.grid(linewidth=0.4, axis="y", zorder=0)
    
    # plt.legend(prop=font_prop1, loc=_legend_pos)

def plot_data_latency(_x_ticks, _x_coordinates, _set_average, _set_p99, _get_average, _get_p99, _colors, _line_labels,
                      _markers, _filename, _legend_pos, _figure_size, _dpi):
    plt.figure(figsize=_figure_size, dpi=_dpi)
    plt.subplot(221)
    plot_line1(_x_ticks, _x_coordinates, _set_average, _colors, "Data Size(Bytes)", "Redis SET Average Latency(ms)",
              _line_labels, _markers, _legend_pos)
    plt.subplot(222)
    plot_line2(_x_ticks, _x_coordinates, _set_p99, _colors, "Data Size(Bytes)", "Redis SET P99 Latency(ms)",
              _line_labels,
              _markers, _legend_pos)
    plt.subplot(223)
    plot_line3(_x_ticks, _x_coordinates, _get_average, colors, "Data Size(Bytes)", "Redis GET Average Latency(ms)",
              _line_labels, _markers, _legend_pos)
    plt.subplot(224)
    plot_line4(_x_ticks, _x_coordinates, _get_p99, _colors, "Data Size(Bytes)", "Redis GET P99 Latency(ms)",
              _line_labels,
              _markers, _legend_pos)
    plt.savefig(_filename, bbox_inches='tight')
    plt.show()
    print("Save redis-latency.pdf")
    plt.clf()

if __name__ == "__main__":
    plt.rc('font', family='Times New Roman', weight='normal', size=15)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['figure.figsize'] = (16.0, 10.0)
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
    _get_average = [
        [0.23, 0.23, 0.228, 0.231, 0.23, 0.229, 0.229, 0.231, 0.227, 0.228, 0.227],
        [0.274, 0.247, 0.239, 0.241, 0.24, 0.242, 0.239, 0.238, 0.241, 0.24, 0.246],
        [0.22, 0.219, 0.219, 0.213, 0.217, 0.222, 0.22, 0.219, 0.223, 0.218, 0.228]
    ]
    _set_average = [
        [0.222, 0.224, 0.228, 0.224, 0.224, 0.22, 0.222, 0.226, 0.229, 0.239, 0.255],
        [0.23, 0.231, 0.238, 0.233, 0.237, 0.228, 0.234, 0.24, 0.237, 0.245, 0.263],
        [0.213, 0.211, 0.21, 0.211, 0.209, 0.204, 0.206, 0.216, 0.219, 0.231, 0.259]
    ]

    _get_p99 = [
        [0.327, 0.327, 0.319, 0.237, 0.327, 0.327, 0.319, 0.327, 0.319, 0.319, 0.319],
        [0.471, 0.327, 0.423, 0.431, 0.423, 0.303, 0.423, 0.423, 0.431, 0.423, 0.431],
        [0.343, 0.335, 0.343, 0.327, 0.343, 0.351, 0.351, 0.351, 0.343, 0.351, 0.351]
    ]
    _set_p99 = [
        [0.311, 0.319, 0.319, 0.319, 0.319, 0.311, 0.311, 0.319, 0.319, 0.327, 0.479],
        [0.423, 0.295, 0.327, 0.423, 0.431, 0.327, 0.423, 0.431, 0.431, 0.447, 0.663],
        [0.351, 0.343, 0.343, 0.335, 0.327, 0.335, 0.335, 0.367, 0.383, 0.423, 0.535]
    ]
    plot_data_latency(x_ticks, x_coordinates, _set_average, _set_p99, _get_average, _get_p99,
                      colors, labels, markers, "./img/redis-latency.pdf", 'best', [16, 11], 80)

    