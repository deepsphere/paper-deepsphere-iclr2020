#!/usr/bin/env python3

from os import path

import numpy as np
from matplotlib import pyplot as plt


plt.rc('font', family='Latin Modern Roman')  # Latin Modern for text
plt.rc('mathtext', fontset='cm')  # Computer Modern for math (default is dejavusans)
#plt.rc('text', usetex=True)
#plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

kernel_width_optimal = {
    8: {
        32:   0.02500,
        64:   0.01228,
        128:  0.00614,
        256:  0.00307,
        512:  0.00154,
        1024: 0.00077,
    },
    20: {
        32:   0.03185,
        64:   0.01564,
        128:  0.00782,
        256:  0.00391,
        512:  0.00196,
        1024: 0.00098,
    },
    40: {
        32:   0.042432,
        64:   0.021354,
        128:  0.010595,
        256:  0.005551,  # seems a bit off
        #512:  0.003028,  # seems buggy
        512:  0.005551 / 2,  # extrapolated
        1024: 0.005551 / 4,  # extrapolated
    },
    60: {
        32:   0.051720,
        64:   0.025403,
        128:  0.012695,
        256:  0.006351,
        #512:  0.002493,  # seems buggy
        512:  0.006351 / 2,  # extrapolated
        1024: 0.006351 / 4,  # extrapolated
    },
}

v1_data = np.load('deepsphere_v1_kernel.npz')
v1_t = v1_data['t']
v1_nside = v1_data['nside']

fig, ax = plt.subplots(figsize=(4, 2.3))
for neighbors, optimums in sorted(kernel_width_optimal.items(), reverse=True):
    nside = np.array([12*n**2 for n in optimums.keys()])
    width = np.array(list(optimums.values()))**2/(4*np.log(2))
    ax.loglog(nside, width, '.-', label=f'$k$-NN graph, $k={neighbors}$')
ax.loglog(12*v1_nside[5:]**2, v1_t[5:], '.--', label=f'Perraudin et al., $k=8$')
ax.legend(loc='upper right')
ax.set_xlabel('$n = 12 N_{side}^2$ pixels', fontsize=14)
ax.set_ylabel('kernel width $t$', fontsize=14)
#ax.set_title('optimal kernel widths')

fig.tight_layout()
filename = path.splitext(path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
