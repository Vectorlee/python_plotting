import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6.2, 5.1))
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(5.6, 5.1))

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42


"""
dataMatrix:  matrix for the heatmap
annotation:  annotation matrix for the heatmap
"""
newMatrix = np.array(dataMatrix)
annotation = np.array(annotation)

sns.heatmap(
    newMatrix,                      # data matrix
    annot=annotation,               # annotation matrix
    fmt="s", 
    annot_kws={'fontsize':'11'},    # annotation attributes
    linewidth=0.5, 
    ax=axes, 
    cbar=False,         # color bar
    cmap=plt.cm.Blues   # color palette
)

axes.set_xticklabels(xlabels, rotation=0)
axes.set_yticklabels(ylabels, rotation=0)

# remove ticks
axes.tick_params(axis='both', which='both', length=0, labelsize='11')
plt.tight_layout()

#fig.savefig('graph.pdf')
