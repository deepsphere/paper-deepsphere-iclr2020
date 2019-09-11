#!/usr/bin/env python3
# coding: utf-8


import os

import numpy as np
from matplotlib import pyplot as plt
import pygsp as pg


# plt.rc('font', family='Latin Modern Roman')
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

stations = np.load('ghcn_stations_2010-2014.npz')
data = np.load('ghcn_data_2010-2014_TMAX.npz')

keep = data['valid_days'].flatten()
data = data['data'].reshape(len(stations['id_ghcn']), -1)
data = data[:, keep]
data = data / 10

# Show the same stations as for the temperature plot.
year, month, day = 2014, 1, 1
t = (year-2010)*365 + (month-1)*30 + (day-1)
keep = ~np.isnan(data[:, t])

data = data[keep]
lon = stations['lon'][keep]
lat = stations['lat'][keep]

print('n_stations: {}, n_days: {}'.format(*data.shape))

# Rotate the view.
lon -= 50
lat -= 20

lon *= np.pi / 180
lat *= np.pi / 180

x = np.cos(lat) * np.cos(lon)
y = np.cos(lat) * np.sin(lon)
z = np.sin(lat)

positions = np.stack([x, y, z], axis=1)
graph = pg.graphs.NNGraph(positions, k=20)
print(graph)

graph.set_signal(np.clip(data[:, t], -20, 40), 'temperature')

graph = graph.subgraph(x > 0)
print(graph)

graph.plotting.update({
    'elevation': 0,
    'azimuth': 0,
    'distance': 8,
    'vertex_size': 10,
    'vertex_color': (0, 0, 0, 1),
    'edge_color': (0.5, 0.5, 0.5, 0.2),
})

graph.coords = graph.coords[:, 1:]

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(1, 1, 1)
graph.plot(edges=True, title='graph of GHCN stations', ax=ax)
#fig, ax = graph.plot(graph.signals['temperature'], edges=True, title='')
#ax.scatter(graph.coords[:, 0], graph.coords[:, 1], 10, graph.signals['temperature'], cmap='RdYlBu_r')
ax.axis('equal')
ax.axis('off')

#fig.tight_layout()
filename = os.path.splitext(os.path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
