
%matplotlib inline 
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from matplotlib import colors as mcolors

"""
Code to generate submission compilance graph
"""
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 3.1))

"""
dataList: is the input data for the graph 
	A list of tuple, where each tuple represents a row
"""
df = pd.DataFrame(data=dataList, columns=['data group', 'data point'])

axes = sns.boxplot(
    x='data group', y='data point', 
	data=df,
    ax=axes, 
    orient='h',         # the orientation of the graph, 'h' will make the graph horizontal
    showfliers=False,   # the outliers of the distribution
    width=[0.8],        # box width
    color='lightgrey',  # box color
    whiskerprops=dict(linestyle='-',linewidth=0, color='white'),    # the line that stretch out: 0~25% and 75~100% 
    capprops=dict(linestyle='-',linewidth=0, color='white'),        # the line that mark the total distribution
    order=box_order     # the display order of the box graph
)

#axes.set_xticklabels(xtickslabels, rotation=30, ha="right")
#axes.set_yticklabels(ytickslabels, rotation=0,  ha='top')
axes.set_xlabel('X Labels', fontsize=12)
axes.set_ylabel('Y Labels', fontsize=12)

#plt.xticks(np.arange(0, 12, 1))
#plt.yticks(np.arange(0, 31, 5))
axes.set_xlim(xmax=380, xmin=-48)
axes.set_ylim(ymax=-0.7, ymin=7.7)

# minor ticks
axes.xaxis.set_minor_locator(ticker.MultipleLocator(6))
axes.tick_params(axis='x', which='major', width=1.2)
axes.tick_params(axis='y', which='both', left=False, right=False)

# grid
axes.grid(color='gray', linestyle=':', linewidth=0.5)
axes.set_axisbelow(True)

plt.tight_layout()
#fig.savefig('graph.pdf')
