import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4.5))

linestyles = ['-', '--', ':', '-.']
markerstyles = ['.', ',', 'o', 'v', '^', '*']
current_palette = ['b', 'g', 'r', 'c', 'm', 'y', 'k']


for i, tag in enumerate(line_dict.keys()):
    X  = np.arange(len(line_dict[tag]))
    Y  = line_dict[tag]
    line = ax.plot(X, Y, linestyle=linestyles[i % 4], color=current_palette[i % 7], label=tag, marker=markerstyles[i % 6])
    plt.setp(line, linewidth=1)


#plt.xticks(np.arange(0, 12, 1))
#plt.yticks(np.arange(0, 1.05, 0.1))
ax.set_xlim(0, 100)
ax.set_ylim(0, 120)
ax.legend(loc=1, frameon=False, fontsize=10)

ax.set_xlabel('Number of Y', fontsize=12)
ax.set_ylabel('Number of X', fontsize=12)

# direction of the ticks
plt.tick_params(axis='x', which='both', bottom='on', top='off')
plt.tick_params(axis='y', which='both', right='off', left='on')

ax.grid(color='gray', linestyle=':', linewidth=0.5)

plt.tight_layout()
#plt.savefig('attacker_ip_shared.pdf')
