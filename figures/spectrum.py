#!/usr/bin/env python3

from os import path
import pickle

import numpy as np
from matplotlib import pyplot as plt
import h5py
import pyshtools

# plt.rc('font', family='Latin Modern Roman')  # Latin Modern for text
# plt.rc('mathtext', fontset='cm')  # Computer Modern for math (default is dejavusans)
# plt.rc('text', usetex=True)
# plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

def plot_with_std(x, y, color=None, alpha=0.2, ax=None, **kwargs):
    ystd = np.std(y, axis=0)
    ymean = np.mean(y, axis=0)
    if ax is None:
        ax = plt.gca()
    lines = ax.plot(x, ymean, color=color, **kwargs)
    color = lines[0].get_color()
    ax.fill_between(x, ymean - ystd, ymean + ystd, alpha=alpha, color=color)
    return ax

def compute_spectrum_climate():
    # Data is from year, month, day, hour, run = 2106, 1, 1, 0, 1
    h5f = h5py.File('example_climate_data.h5', mode='r')
    data = h5f['climate']['data']  # (16,768,1152) numpy array
    spectrum = list()
    for d in data:
        d = d[::2, ::3]  # Make it square (needed for pyshtools).
        d = (d - d.min()) / (d.max() - d.min()) * 2 - 1  # Standardize.
        grid = pyshtools.SHGrid.from_array(d, grid='DH')
        clm = grid.expand(normalization='4pi')
        spectrum.append(clm.spectrum())
    return spectrum

# 1000 objects out of 30k were randomly sampled to be analyzed.
# The mean was subtracted from each signal in a preprocessing step.
# The spectrum was computed by healpy.anafast up to lmax=nside (since there's nothing beyond).
# cl is a dictionary with keys = {0, 1, 2}. cl[feature] is a matrix of shape [1000, 33] where each row is the spectrum of one signal.
spectrum_shrec17 = pickle.load(open('spectrum_shrec17.pickle', 'rb'))
spectrum_shrec17 = np.vstack([
    spectrum_shrec17[0],
    spectrum_shrec17[1],
    spectrum_shrec17[2],
])

spectrum_cosmo = np.load('spectrum_cosmo.npz')
spectrum_cosmo = np.vstack([
    spectrum_cosmo['psd_class1'],
    spectrum_cosmo['psd_class2'],
])

# One spectrum per variable (e.g., TMQ, U850, V850, etc.).
# There doesn't seem to be much variation across dates or runs.
spectrum_climate = compute_spectrum_climate()
spectrum_climate = np.vstack(spectrum_climate)

fig, ax = plt.subplots(figsize=(5, 2.5))

spectrums = [
    (spectrum_shrec17, "SHREC'17 (depth and normal)"),
    (spectrum_cosmo, 'cosmology (convergence map)'),
    (spectrum_climate, 'climate (16 variables)'),
]
for spectrum, label in spectrums:
    print("{}: {} maps with degree at most {}".format(label, *spectrum.shape))
    #l = np.arange(spectrum.shape[1])
    y = np.mean(spectrum, axis=0) # *l*(l+1)
    scale = np.mean(y[:33])  # or y[1]
    ax.plot(y / scale, label=label)
    #plot_with_std(l, spectrum/scale, ax=ax, label=label)

ax.legend(loc='upper right')
ax.set_xlim([1, 1e3])
ax.set_ylim([1e-3, 5e1])
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('spherical harmonic degree $\ell$', fontsize=14)
#ax.set_ylabel('power spectrum $C_\ell$')
ax.set_ylabel('power spectrum', fontsize=14)
#ax.set_ylabel('$C_\ell \cdot \ell \cdot (\ell+1)$')
#ax.set_title('Power Spectrum Density, 3-arcmin smoothing, noiseless, Nside=1024')

fig.tight_layout()
filename = path.splitext(path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
