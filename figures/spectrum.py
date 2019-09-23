#!/usr/bin/env python3

from os import path
import pickle

import numpy as np
from matplotlib import pyplot as plt

#plt.rc('font', family='Latin Modern Roman')
#plt.rc('text', usetex=True)
#plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

def plot_with_std(x, y, color=None, alpha=0.2, ax=None, **kwargs):
    ystd = np.std(y, axis=0)
    ymean = np.mean(y, axis=0)
    if ax is None:
        ax = plt.gca()
    lines = ax.plot(x, ymean, color=color, **kwargs)
    color = lines[0].get_color()
    ax.fill_between(x, ymean - ystd, ymean + ystd, alpha=alpha, color=color)
    return ax

# 1000 objects out of 30k were randomly sampled to be analyzed.
# The mean was subtracted from each signal in a preprocessing step.
# The spectrum was computed by healpy.anafast up to lmax=nside (since there's nothing beyond).
# cl is a dictionary with keys = {0, 1, 2}. cl[feature] is a matrix of shape [1000, 33] where each row is the spectrum of one signal.
spectrum_shrec17 = pickle.load(open('../figures/spectrum_shrec17.pickle', 'rb'))
spectrum_shrec17 = np.vstack([
    spectrum_shrec17[0],
    spectrum_shrec17[1],
    spectrum_shrec17[2],
])

spectrum_cosmo = np.load('../figures/spectrum_cosmo.npz')
spectrum_cosmo = np.vstack([
    spectrum_cosmo['psd_class1'],
    spectrum_cosmo['psd_class2'],
])

print("SHREC'17: {} maps with degree at most {}".format(*spectrum_shrec17.shape))
print("cosmo: {} maps with degree at most {}".format(*spectrum_cosmo.shape))

fig, ax = plt.subplots(figsize=(5, 2.5))

l = np.arange(spectrum_shrec17.shape[1])
y = np.mean(spectrum_shrec17, axis=0) # *l*(l+1)
scale = np.mean(y[:33])  # or y[1]
ax.plot(l, y / scale, label="SHREC'17 (depth and normal maps)")
#plot_with_std(l, spectrum_shrec17/scale, ax=ax, label="SHREC'17 (depth and normal maps)")

l = np.arange(spectrum_cosmo.shape[1])
y = np.mean(spectrum_cosmo, axis=0) # *l*(l+1)
scale = np.mean(y[:33])  # or y[1]
ax.plot(l, y / scale, label='cosmology (convergence map)')
#plot_with_std(l, spectrum_cosmo/scale, ax=ax, label="cosmology (convergence map)")

ax.legend()
ax.set_xlim([1, 1e3])
ax.set_ylim([1e-3, 5e1])
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('$\ell$: spherical harmonic index')
ax.set_ylabel('$C_\ell$: power spectrum')
#ax.set_ylabel('$C_\ell \cdot \ell \cdot (\ell+1)$')
#ax.set_title('Power Spectrum Density, 3-arcmin smoothing, noiseless, Nside=1024')

fig.tight_layout()
filename = path.splitext(path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
