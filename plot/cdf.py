import matplotlib.pyplot as plt
import numpy as np
import copy
import csv
from matplotlib.font_manager import FontProperties
import pandas as pd
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter

plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

def plot_line(_x_ticks, _x_coordinates, _data, _colors, _x_label, _y_label, _line_labels,
              _markers, _legend_pos):
    types = len(_data)
    # Set ticks
    font_prop1 = FontProperties(family='Times New Roman', weight='normal', size=12)
    font_prop2 = FontProperties(family='Times New Roman', weight='normal', size=15)
    plt.xticks(_x_coordinates, _x_ticks)
    xtick_labels = plt.gca().get_xticklabels()
    ytick_labels = plt.gca().get_yticklabels()
    [xtick_label.set_fontproperties(font_prop1) for xtick_label in xtick_labels]
    [ytick_label.set_fontproperties(font_prop2) for ytick_label in ytick_labels]

    # Set x, y labels
    plt.xlabel(_x_label, {'family': 'Times New Roman', 'weight': 'bold', 'size': 20}, labelpad=8)
    plt.ylabel(_y_label, {'family': 'Times New Roman', 'weight': 'bold', 'size': 20})
    plt.xlim([0.5, 30.5])
    plt.ylim([0.001, 1.03])
    plt.grid(linewidth=0.4, axis="y", zorder=0)
    # plt.title(title, {'family': 'Times New Roman', 'weight': 'bold', 'size': 14})

    # plot
    plt.plot(_x_coordinates, _data[0], color=_colors[0], marker=_markers[0], label=_line_labels[0], linewidth=2, markersize=6.5)
    plt.plot(_x_coordinates, _data[1], color=_colors[1], marker=_markers[1], label=_line_labels[1], linewidth=2, markersize=6.5)
    plt.plot(_x_coordinates, _data[2], color=_colors[2], marker=_markers[2], label=_line_labels[2], linewidth=2)
    plt.plot(_x_coordinates, _data[3], color=_colors[3], marker=_markers[3], label=_line_labels[3], linewidth=2, markersize=6.5)
    plt.plot(_x_coordinates, _data[4], color=_colors[4], marker=_markers[4], label=_line_labels[4], linewidth=2)
    plt.legend(prop=font_prop1, loc=_legend_pos)
    plt.legend(framealpha=1.0, prop=font_prop1, frameon=True, ncol=3, bbox_to_anchor=(0.9, 1.2))

def plot_cdf(_x_ticks, _x_coordinates, _colors, _line_labels,_markers, _filename, _legend_pos):
    _data = [['0', '0', '324', '94065', '5539', '28', '13', '8', '5', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '2', '4', '4', '4', '17', '52', '98', '537', '1938', '2884', '17505', '36515', '14456', '7582', '2354', '842'],
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '11', '187', '432', '40556', '26632', '15646', '8961', '193', '128', '3099', '1820', '1584', '597'],
['0', '0', '0', '0', '1376', '49212', '13374', '5791', '17137', '5413', '2222', '2577', '2056', '645', '159', '37', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
['0', '0', '1703', '3578703', '19593', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]

    cdfs = []
    data = []
    for lines in _data:
        sum = 0
        for num in lines:
            sum += int(num)
        for i in range(len(lines)):
            lines[i] = float(int(lines[i]) / sum)
        data.append(lines)

    for num in data:
        cdf = np.cumsum(num)
        cdfs.append(cdf)
    plot_line(_x_ticks, _x_coordinates, cdfs, _colors, "Schedule Latency(us)", "CDF",
              _line_labels,
              _markers,
              _legend_pos)
    plt.savefig("./img/"+_filename, bbox_inches='tight')
    plt.show()
    print("Save recv.pdf")
    plt.clf()

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['figure.figsize'] = (8.0, 5.0)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 100
    # draw recv side figure
    x_coordinates = np.array(range(1, 12, 1))
    x_ticks = ["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096"]
    # [orange gold purple green blue]
    colors = ["#F59D56", "#FFD066", "#7F659F", "#C4D6A0", "#93CDDD"]
    markers = ['X', 'p', 'o', 'v', 's']
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

    _client_get = [
        [3721,3721,3713,3700,3701,3661,3595],
        [3725,3725,3723,3723,3723,3724,3722],
    ]
    x_coordinates = np.array(range(1, 8, 1))
    x_ticks = ["0", "5", "10", "15", "20", "25", "30"]
    labels = ["KVM", "Hummer", "BSD-PIPE", "BSD-TCP"]

    x_coordinates = np.array(range(1, 31, 1))
    x_ticks = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "13", "14", "15", "16", "17", "18", "19", "20","21", "22", "23", "24", "25", "26", "27", "28", "29"]
    # [orange gold purple green blue]
    colors = ["#F59D56", "#FFD066", "#7F659F", "#C4D6A0", "#93CDDD"]
    markers = ['^', 'D', 'o', 'v', 's']
    labels = ["Bare-Metal", "KVM", "KVM(CPU-PIN)", "KVM(Real-Time)", "Hummer"]


    plot_cdf(x_ticks, x_coordinates, colors, labels, markers, "./cdf.pdf",'best')

    # Original Redis 4M GET/SET request latency and percentage of each period
    """
    SIZE             BuildREQ  TransferREQ  HandleREQ  TransferREPLY  ProcessREPLY     
    Sandbox-TCP         ---         ---        ---          ---           ---
    CheriBSD-TCP        ---         ---        ---          ---           ---
    Sandbox-SCST        ---         ---        ---          ---           ---
    """

    labels = ["Bare-Metal", "KVM", "Hummer"]
    x_labels = ["Dhrystone","Whetstone","Execl","Pipe","Shell"]
    # [orange green purple red blue]
    # colors = ["#FF7F0D", "#2CA12C", "#7F659F", "#A21C1D", "#1F77B4"]
    # colors = ["w", "w", "w", "w", "#1F77B4"]
    colors = [ "#E5FFDF", "#FFF2CC", "#C9EAF2", "#EBEFFF", "#EAD1DC" ]
    hatches = ['//', '*', 'XX', '......', '00']

    _unixbench_data_single = [
        [3049, 1181, 661, 165, 1310],
        [3021, 1146, 642, 166, 1273],
        [3033, 1171, 658, 195, 1297]
    ]

    _unixbench_data_multi = [
        [12041,4724,2695,1468,5689],
        [11921,4583,2357,1452,5642],
        [12026,4690,2569,1458,5692]
    ]

    labels = ["Bare-Metal", "KVM", "KVM PV-IPI", "Hummer"]
    x_labels = ["Normal IPI", "Broadcast IPI"]

    _ipi_data = [
        [996,0],
        [3003,2998],
        [2955,2626],
        [2063,2892]
    ]

    labels = ["Bare-Metal", "KVM", "Hummer"]
    x_labels = ["1", "2", "4", "8"]

    cpu_data = [
        [932,1859,3718,3727],
        [931,1862,3725,3725],
        [932,1864,3725,3724]
    ]

    mem_data = [
        [16852,1717,9309,1732],
        [16852,1717,9309,1732],
        [16977,1725,9499,1736]
    ]
    x_labels = ["Seq Read", "Rnd Read", "Seq Write", "Rnd Write"]


    y_labels = ["SBX-TCP", "BSD-TCP", "SBX-SCST"]
    bar_labels = ["Build REQ", "Trans REQ", "Handle REQ", "Trans RREPLY", "Handle REPLY"]
    # [orange green purple red blue]
    colors = ["#FF7F0D", "#2CA12C", "#7F659F", "#A21C1D", "#1F77B4"]
    hatches = ['OO', '++', 'xx', 'X*', '//']
    set_period_latency = [
        [582.74, 10189.43, 159.31, 4.42, 0.89],
        [341.11, 705.76, 5.36, 2.43, 2.30],
        [697.14, 250.89, 8.56, 21.77, 21.98],
    ]

    set_percentage = [
        [5.33, 93.17, 1.46, 0.04, 0.01],
        [32.27, 66.77, 0.51, 0.23, 0.22],
        [69.69, 25.08, 0.86, 2.18, 2.20]
    ]

    get_period_latency = [
        [1.04, 81.85, 221.20, 22680.60, 0.95],
        [2.67, 2.96, 138.74, 957.18, 2.57],
        [1.17, 5.65, 54.40, 640.21, 42.07]
    ]

    get_percentage = [
        [0.00, 0.36, 0.96, 98.67, 0.00],
        [0.34, 0.27, 12.57, 86.69, 0.23],
        [0.16, 0.76, 7.32, 86.11, 5.66]
    ]

    # Optimized Redis 4M GET/SET request latency and percentage of each period
    y_labels = ["SBX-TCP", "SBX-TCP-OPT", "BSD-TCP", "SBX-SCST", "SBX-SCST-OPT"]

    set_period_latency = [
        [582.74, 10189.43, 159.31, 4.42, 0.89],
        [274.07, 8876.96, 5.11, 11.21, 6.52],
        [341.11, 705.76, 5.36, 2.43, 2.30],
        [697.14, 250.89, 8.56, 21.77, 21.98],
        [218.51, 54.30, 4.66, 15.83, 0.74],
    ]

    set_percentage = [
        [5.33, 93.17, 1.46, 0.04, 0.01],
        [2.99, 96.76, 0.06, 0.12, 0.07],
        [32.27, 66.77, 0.51, 0.23, 0.22],
        [69.69, 25.08, 0.86, 2.18, 2.20],
        [74.31, 18.47, 1.59, 5.38, 0.25]
    ]

    get_period_latency = [
        [1.04, 81.85, 221.20, 22680.60, 0.95],
        [0.98, 11.71, 119.60, 20979.26, 0.93],
        [2.67, 2.96, 138.74, 957.18, 2.57],
        # [1.17, 5.65, 54.50, 32.49, 649.79],
        [1.17, 5.65, 54.40, 640.21, 42.07],
        [1.12, 4.36, 54.13, 258.00, 11.01]
    ]

    get_percentage = [
        [0.00, 0.36, 0.96, 98.67, 0.00],
        [0.00, 0.06, 0.57, 99.37, 0.00],
        [0.34, 0.27, 12.57, 86.69, 0.23],
        # [0.16, 0.76, 7.32, 4.37, 87.40],
        [0.16, 0.76, 7.32, 86.11, 5.66],
        [0.34, 1.33, 16.47, 78.51, 3.35]
    ]
