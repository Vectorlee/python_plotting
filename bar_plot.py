import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker


"""
collection: the order to display different bars
category_list: different categories (stacked bars) within each bar
"""
bar_list = []
for index in range(len(category_list)):
    bar_items = []
    for feed in collection:
        bar_items.append(category_cdf_dict[feed][index])
    bar_list.append(bar_items)


fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6.1, 4.5))

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

linestyles = ['-', '--', ':']
current_palette = ['seagreen', '#8856a7', 'darkgoldenrod', 'firebrick', '#2c7fb8', '#66c2a5']


"""
stack bar graph are being plotted layer by layer
first round:            second round:
|                       |
|                       |     1     1
|  1  1  1  1           |  1  1  1  1
|________________       |______________
"""
for index, bar_items in reversed(list(enumerate(bar_list))):
    tag = category_list[index]
    axes.bar(range(len(collection)), bar_items, color=current_palette[index % 7], edgecolor='white', label=tag)
    

#axes.set_ylim(0, 60)
plt.xticks(np.arange(len(collection)))
plt.yticks(np.arange(0, 52, 10))

# set minor ticks
axes.yaxis.set_minor_locator(ticker.MultipleLocator(2))

axes.legend(loc=1, frameon=False, fontsize=12, ncol=2)

axes.set_xticklabels(collection, fontsize=12) #, rotation=0, ha="right")
#axes.set_yticklabels([0, 20, 40, 60, 80, 100, ''], fontsize=11)

axes.set_xlabel('Bars', fontsize=12)
axes.set_ylabel('Values', fontsize=12)

axes.tick_params(axis='y', which='both', direction='in')

plt.tight_layout()
#fig.savefig('perfect_org_breakdown.svg')
