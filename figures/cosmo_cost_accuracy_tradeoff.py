#!/usr/bin/env python3

from os import path

from matplotlib import pyplot as plt

#plt.rc('font', family='Latin Modern Roman')
#plt.rc('text', usetex=True)
#plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

neighbors = [8, 20, 40]
accuracy = [87.1, 91.3, 92.5]
speed = [185, 250, 363]
fig, ax = plt.subplots(figsize=(3, 2.74))
ax.plot(speed, accuracy, '.-')
ax.set_xlabel('inference time [ms]')
ax.set_ylabel('accuracy [%]')
for x, y, k in zip(speed, accuracy, neighbors):
    align = 'right' if k == 40 else 'left'
    ax.text(x, y-1.1, f'$k={k}$', horizontalalignment=align)
#ax.set_ylim(86, 93)

x, y, label = 187, 83.8, 'FCN variant'
ax.scatter(x, y, c=(1, 0, 0), marker='x')
ax.text(x, y+0.5, label, horizontalalignment='left')

fig.tight_layout()
filename = path.splitext(path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
