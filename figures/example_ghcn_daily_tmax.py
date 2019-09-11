#!/usr/bin/env python3
# coding: utf-8

# # DAILY GLOBAL HISTORICAL CLIMATOLOGY NETWORK (GHCN-DAILY)
#
# Version 3.24
#
# [Andreas Loukas](https://andreasloukas.wordpress.com/), [EPFL LTS2](https://lts2.epfl.ch/), [Michaël Defferrard](http://deff.ch)
#
# Menne, M.J., I. Durre, B. Korzeniewski, S. McNeal, K. Thomas, X. Yin, S. Anthony, R. Ray,
# R.S. Vose, B.E.Gleason, and T.G. Houston, 2012: Global Historical Climatology Network -
# Daily (GHCN-Daily), Version 3.
#
# The five core features are:
#
# * PRCP = Precipitation (tenths of mm)
# * SNOW = Snowfall (mm)
# * SNWD = Snow depth (mm)
# * TMAX = Maximum temperature (tenths of degrees C)
# * TMIN = Minimum temperature (tenths of degrees C)
#
# [FTP link](ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/)


import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import cartopy.crs as ccrs


# plt.rc('font', family='Latin Modern Roman')
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

years = np.arange(2010, 2015)
n_years = len(years)

# Load station data

stations = np.load('ghcn_stations_{:4d}-{:4d}.npz'.format(years[0], years[-1]))
n_stations = len(stations['id_ghcn'])
print('{} weather stations identified.'.format(n_stations))

# Load station measurements

feature_name = 'TMAX'
filename = 'ghcn_data_{:4d}-{:4d}_{}.npz'.format(years[0], years[-1], feature_name)
data_file = np.load(filename)
data, valid_days = data_file['data'], data_file['valid_days']
n_stations = data.shape[0]
print(f'{n_stations} stations loaded.')

# Data inspection

# Reshape our data array from (years, months, days) into a timeseries
data = data.reshape((n_stations, n_years*12*31))

# change to Celsius
if feature_name in ['TMIN', 'TMAX']:
    data = data / 10

# keep only valid days (i.e., days for which we have data)
day_mask = np.squeeze(valid_days.reshape(n_years*12*31))
data = data[:, day_mask]
n_stations, n_days = data.shape
print(f'n_stations: {n_stations}, n_days: {n_days}')

# Discard stations that do not report measurements during this period
# keep = ~np.isnan(data).any(axis=1) # keep a station if we have measurements for each day in the period of interest
keep = ~np.isnan(data).all(axis=1) # keep a station if we have at least one measurement in the period of interest

data = data[keep]
n_stations, n_days = data.shape
print(f'n_stations: {n_stations}, n_days: {n_days}')

# Figure

fig = plt.figure(figsize=(4, 4))
#ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Orthographic(50, 20))
ax.set_global()
ax.coastlines(linewidth=2)
#ax.stock_img()

year, month, day = 2014, 1, 1
t = (year-2010)*365 + (month-1)*30 + (day-1)

zmin, zmax = -20, 40

#plt.scatter(stations['lon'][keep], stations['lat'][keep], s=None, c=data[:, t], cmap=plt.get_cmap('RdYlGn'))
sc = ax.scatter(stations['lon'][keep], stations['lat'][keep], s=10,
                c=np.clip(data[:, t], zmin, zmax), cmap=plt.get_cmap('RdYlBu_r'),
                vmin=zmin, vmax=zmax, alpha=1, transform=ccrs.PlateCarree())

ticks = range(zmin, zmax+1, 20)
cb = fig.colorbar(sc, ax=ax, orientation='horizontal', fraction=0.02, aspect=40, pad=0.03, ticks=ticks)
cb.ax.tick_params(labelsize=10)
cb.ax.set_xticklabels([f'${t}^\circ C$' for t in ticks])

#ax.set_title(f'GHCN-daily, TMAX, {year}-{month:02d}-{day:02d}')
ax.text(0, 7e6, f'GHCN-daily, TMAX, {year}-{month:02d}-{day:02d}', horizontalalignment='center')

#fig.tight_layout()
filename = os.path.splitext(os.path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
