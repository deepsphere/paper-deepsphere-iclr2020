#!/usr/bin/env python3

from os import path
import pickle

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


fig, ax = plt.subplots(figsize=(9, 9))

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }
plt.rcParams.update({'font.size': 18})

# -------------- khasanova-Frossard ------------------

equiv_error_KF = pickle.load(open('equivariance_error/khasanova_frossard.pickle', 'rb'))

markers = ['v', 'x', 'o']

degree_step = {
    32: 3,
    64: 6,
    128: 12,
    256: 25,
}

for bw, marker in zip([64, 128, 256], markers):
    lmax = bw
    degrees = np.arange(0, lmax, degree_step[bw])
    degrees = degrees[1:]
    ax.loglog(degrees, equiv_error_KF[bw][1:], f'm{marker}-')

# ----------------- healpix ----------------------

equiv_error_V1 = pickle.load(open('equivariance_error/V1 - ||Lf||.pickle', 'rb'))
equiv_error_8 = pickle.load(open('equivariance_error/V2 - 8 neighbors - ||Lf||.pickle', 'rb'))
equiv_error_20 = pickle.load(open('equivariance_error/V2 - 20 neighbors - ||Lf||.pickle', 'rb'))
equiv_error_40 = pickle.load(open('equivariance_error/V2 - 40 neighbors - ||Lf||.pickle', 'rb'))

nsides = [32, 64, 128]

degree_step = {
    32: 10,
    64: 10,
    128: 50,
    256: 50,
    512: 100,
    1024: 200,
}

for nside, marker in zip(nsides, markers):
    lmax = 3 * nside - 1
    degrees = np.arange(0, lmax+1, degree_step[nside])
    degrees = degrees[1:]
    ax.loglog(degrees, equiv_error_V1[nside][1:], f'g{marker}-')
    ax.loglog(degrees, equiv_error_8[nside][1:], f'c{marker}-')
    ax.loglog(degrees, equiv_error_20[nside][1:], f'r{marker}-')
    ax.loglog(degrees, equiv_error_40[nside][1:], f'b{marker}-')

# -------------- final parameters ------------------

ax.set_xlabel(r'spherical harmonic degree $\ell$', fontdict=font,)
#ax.set_ylabel(r'mean equivariance error $\overline{E}_{\mathbf{L}, C}$', fontdict=font, )
ax.set_ylabel(r'mean equivariance error $\overline{E}_{L, C}$', fontdict=font, )

ax.tick_params(axis='both', which='major')
ax.grid()
ax.set_xlim([10, np.max(degrees)])

# Add first legend: only labeled data is included
# ax.legend(prop={'size': 20})
handles = [  # Some fake handles.
    Line2D([0], [0], color='m', marker='', markersize=8),
    Line2D([0], [0], color='g', marker='', markersize=8),
    Line2D([0], [0], color='c', marker='', markersize=8),
    Line2D([0], [0], color='r', marker='', markersize=8),
    Line2D([0], [0], color='b', marker='', markersize=8),
]
labels = ['Khasanova & Frossard, $k=4$', 'Perraudin et al., $k=8$']
labels.extend([f'$k$-NN graph, $k={k}$ neighbors' for k in [8, 20, 40]])
legend = ax.legend(handles, labels, loc='lower left')
ax.add_artist(legend)  # Manually add the first legend back

# Add second legend for the maxes and mins.
handles = [  # Some fake handles.
    Line2D([0], [0], color='k', marker='v', markersize=8),
    Line2D([0], [0], color='k', marker='x', markersize=8),
    Line2D([0], [0], color='k', marker='o', markersize=8),
]
labels = [rf'$n \propto {s}^2$' for s in [32, 64, 128]]
ax.legend(handles, labels, loc='upper right')

fig.tight_layout()
filename = path.splitext(path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
