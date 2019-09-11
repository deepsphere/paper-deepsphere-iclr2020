#!/usr/bin/env python3

"""
From https://martinos.org/mne/dev/auto_tutorials/plot_visualize_evoked.html
"""

import os

import matplotlib.pyplot as plt
import mne

# plt.rc('font', family='Latin Modern Roman')
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

data_path = mne.datasets.sample.data_path()
fname = os.path.join(data_path, 'MEG', 'sample', 'sample_audvis-ave.fif')
evoked = mne.read_evokeds(fname, baseline=(None, 0), proj=True)

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(1, 1, 1)
evoked[0].plot_topomap(times=0.1, show=False, colorbar=False, axes=ax)#, contours=False)
ax.set_title('MEG evoked potential, $0.1s$')
#cb = fig.colorbar(ax.collections[-1], ax=ax, orientation='horizontal', fraction=0.02, aspect=40, pad=0.03)#, ticks=ticks)

fig.tight_layout()
filename = os.path.splitext(os.path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
