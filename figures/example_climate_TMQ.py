#!/usr/bin/env python3

r"""Climate event detection

Simulation data from the HAPPI20 run of the Community Atmospheric Model (CAM5).

URLs:
* https://portal.nersc.gov/project/dasrepo/deepcam/segm_h5_v3_reformat/gb_data_readme
* https://github.com/hpcac/ISC19-SCC

The 16 features are:

01. TMQ: Total (vertically integrated) precipitable water [kg/m^2]
         the total amount of water vapor at that lat/lon grid cell
02. U850: Zonal wind at 850 mbar pressure surface [m/s]
03. V850: Meridional wind at 850 mbar pressure surface [m/s]
04. UBOT: lowest level zonal wind [m/s]
05. VBOT: Lowest model level meridional wind [m/s]
06. QREFHT: reference height humidity [kg/kg]
07. PS: surface pressure [Pa]
08. PSL: sea level pressure [Pa]
09. T200: temperature at 200 mbar pressure surface [K]
10. T500: temperature at 500 mbar pressure surface [K]
11. PRECT: total (convective and large-scale) precipitation rate (liq + ice) [m/s]
12. TS: surface temperature (radiative) [K]
13. TREFHT: reference height temperature [K]
14. Z1000: geopotential Z at 1000 mbar pressure surface [m]
           the height (in meters) corresponding to 1000 mbar of pressure
15. Z200: geopotential Z at 200 mbar pressure surface [m]
          the height (in meters) corresponding to 200 mbar of pressure
16. ZBOT: lowest modal level height [m]

resolution of 768 x 1152 equirectangular grid (25-km at equator)

The labels are 0 for background class, 1 for tropical cyclone (TC), and 2 for atmoshperic river (AR)
"""


import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import h5py


# plt.rc('font', family='Latin Modern Roman')  # Latin Modern for text
# plt.rc('mathtext', fontset='cm')  # Computer Modern for math (default is dejavusans)
# plt.rc('text', usetex=True)
# plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

# Load simulation data

year, month, day, hour, run = 2106, 1, 1, 0, 1
filename = 'data-{}-{:0>2d}-{:0>2d}-{:0>2d}-{}.h5'.format(year, month, day, hour, run)
url = f'https://portal.nersc.gov/project/dasrepo/deepcam/segm_h5_v3_reformat/{filename}'
print(f'using data from {url}')
# that file was saved as example_climate_data.h5
h5f = h5py.File('example_climate_data.h5', mode='r')
labels = h5f['climate']['labels']  # (768,1152) numpy array
data = h5f['climate']['data']  # (16,768,1152) numpy array
data = data[0]  # first field is TMQ

lon = np.arange(1152) / 1152 * 360
lat = np.arange(768) / 768 * 180 - 90
lon, lat = np.meshgrid(lon, lat)

# Figure

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Orthographic(90, 0))
ax.set_global()
ax.coastlines(linewidth=2)

sc = plt.scatter(lon, lat, c=data, s=1, rasterized=True, vmin=0,
                 cmap=plt.get_cmap('RdYlBu_r'), transform=ccrs.PlateCarree())
ticks = [0, 40, 80]
cb = plt.colorbar(sc, ax=ax, orientation='horizontal', anchor=(1, 0), shrink=0.7, pad=0.05, ticks=ticks)
cb.ax.set_xticklabels([f'${t} \, kg/m^2$' for t in ticks])

TC = (labels[:, :] == 1)
AR = (labels[:, :] == 2)
ax.scatter(lon[AR], lat[AR], s=0.5, marker='s', color='g', edgecolors='none', label='AR', alpha=1, transform=ccrs.PlateCarree())
ax.scatter(lon[TC], lat[TC], s=0.5, marker='s', color='m', edgecolors='none', label='TC', alpha=1, transform=ccrs.PlateCarree())
ax.legend(markerscale=10, frameon=False, bbox_to_anchor=(0.15, 0.18))

ax.text(0, 7e6, f'CAM5 HAPPI20 run {run}, TMQ, {year}-{month:02d}-{day:02d}', horizontalalignment='center')

fig.tight_layout()
filename = os.path.splitext(os.path.basename(__file__))[0] + '.pdf'
fig.savefig(filename, dpi=150)
