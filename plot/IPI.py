import matplotlib.pyplot as plt
import numpy as np
import copy
import csv
from matplotlib.font_manager import FontProperties
import pandas as pd
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter

def accumulate(data):
    types = len(data)
    # process data list
    periods = len(data[0])
    base = [0.0 for i in range(types)]
    processed_data = [base]
    for i in range(periods - 1):
        tmp = copy.copy(processed_data[-1])
        for j in range(len(tmp)):
            tmp[j] += data[j][i]
        processed_data.append(tmp)
    return processed_data


def transpose(data):
    processed_data = []
    for i in range(len(data[0])):
        tmp = []
        for j in range(len(data)):
            tmp.append(data[j][i])
        processed_data.append(tmp)
    return processed_data


def get_hbar_y(n, dist, h, w):
    y = []
    total_width = (n - 1) * dist + n * w
    c = h / 2
    t = c + total_width / 2 - w / 2
    for i in range(n):
        y.append(t)
        t -= (dist + w)
    return y


def plot_bar(_bar_width, _y_coordinates, _y_ticks, _data, _left, _colors, _bar_labels, _x_label, _hatches, _show_legend,
             _need_log, _height):
    types = len(_data)
    # Set ticks
    plt.ylim(0, _height)
    plt.grid(b=True, axis='x', linewidth=0.7, linestyle='--', zorder=0)
    font_prop1 = FontProperties(family='Times New Roman', weight='normal', size=10)
    font_prop2 = FontProperties(family='Times New Roman', weight='normal', size=10)
    xtick_labels = plt.gca().get_xticklabels()
    ytick_labels = plt.gca().get_yticklabels()
    [xtick_label.set_fontproperties(font_prop1) for xtick_label in xtick_labels]
    [ytick_label.set_fontproperties(font_prop2) for ytick_label in ytick_labels]
    plt.yticks(_y_coordinates, _y_ticks, rotation=-60, verticalalignment='center')

    # Set x y labels
    # plt.ylabel(y_label, {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})
    plt.xlabel(_x_label, {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})

    # plot
    if _need_log:
        plt.xscale('log', base=10)
    for i in range(types):
        plt.barh(_y_coordinates, _data[i], height=_bar_width, color=_colors[i], edgecolor="black",
                 label=_bar_labels[i], left=_left[i], hatch=_hatches[i], zorder=10)

    if _show_legend:
        plt.legend(loc='upper center', bbox_to_anchor=(1, 1.15), ncol=10, prop=font_prop1)


def plot_wbar(_bar_width, _x_ticks, _data, _colors, _bar_labels, _y_label, _x_label,_hatches,size):
    x = np.arange(size)
    # plt.grid(b=True, axis='x', linewidth=0.7, linestyle='--', zorder=0)
    font_prop1 = FontProperties(family='Times New Roman', weight='bold', size=20)
    font_prop2 = FontProperties(family='Times New Roman', weight='normal', size=20)
    font_prop3 = FontProperties(family='Times New Roman', weight='normal', size=15)
    xtick_labels = plt.gca().get_xticklabels()
    ytick_labels = plt.gca().get_yticklabels()
    [xtick_label.set_fontproperties(font_prop1) for xtick_label in xtick_labels]
    [ytick_label.set_fontproperties(font_prop2) for ytick_label in ytick_labels]
    plt.xticks(x, _x_ticks, fontsize=20)
    plt.ylabel(_y_label, {'family': 'Times New Roman', 'weight': 'bold', 'size': 20})
    plt.xlabel(_x_label, {'family': 'Times New Roman', 'weight': 'bold', 'size': 20})
    plt.grid(linewidth=0.4, axis="y", zorder=0)

    total_width, n = 0.8, len(_bar_labels)
    width = total_width / n
    x = x - (total_width - width) / 2

    for i in range(n):
        plt.bar(x + i * width, _data[i], width=width, color=_colors[i], edgecolor="black", label=_bar_labels[i], hatch=_hatches[i],
            zorder=10)
    plt.legend(loc='best', prop=font_prop3)


def plot_IPI(_bar_width, _x_ticks, _data, _colors, _bar_labels,
                   _hatches, _filename, _figure_size, _dpi):
    plt.figure(figsize=_figure_size, dpi=_dpi)
    # plt.plot(_x_ticks, _baremental[0], fillstyle='none', linestyle='--', marker=dot_style[0],markersize=12, linewidth=_bar_width, label=_bar_labels[0], color=colors[0])
    # plot_wbar(_bar_width, get_hbar_y(len(_x_ticks), 0.2, _height, 0.3), _x_ticks, _data,_colors, _bar_labels, "SET Latency(ms)", _hatches, True, False, _height)
    plot_wbar(_bar_width, _x_ticks, _data, _colors, _bar_labels, "IPI Latency(ns)", "", _hatches, 2)

    plt.savefig(_filename, bbox_inches='tight')
    plt.show()
    print("Save recv.pdf")
    plt.clf()


if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['figure.figsize'] = (8.0, 5.0)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 100
    plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

    colors = [ "#E5FFDF", "#FFF2CC", "#C9EAF2", "#EBEFFF", "#EAD1DC" ]
    hatches = ['', '', '', '', '']
    labels = ["Bare-Metal", "KVM", "KVM PV-IPI", "Hummer"]
    x_labels = ["Normal IPI", "Broadcast IPI"]

    _ipi_data = [
        [996,0],
        [3003,2998],
        [2955,2626],
        [2063,2892]
    ]

    plot_IPI(0.2, x_labels, _ipi_data, colors,
                   labels, hatches, "./img/IPI.pdf", (11, 8), 200)