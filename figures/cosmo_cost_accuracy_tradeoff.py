#!/usr/bin/env python3

from os import path

from matplotlib import pyplot as plt

#plt.rc('font', family='Latin Modern Roman')  # Latin Modern for text
plt.rc('mathtext', fontset='cm')  # Computer Modern for math (default is dejavusans)
# plt.rc('text', usetex=True)
# plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

neighbors = [8, 20, 40]
accuracy = [87.1, 91.3, 92.5]
speed = [185, 250, 363]
fig, ax = plt.subplots(figsize=(2.5, 2.25))
ax.plot(speed, accuracy, '.-')
ax.set_xlabel('inference time [ms]')
ax.set_ylabel('accuracy [%]')
#for x, y, k in zip(speed, accuracy, neighbors):
#    align = 'right' if k == 40 else 'left'
#    ax.text(x, y-1.1, f'$k={k}$', horizontalalignment=align)
ax.text(speed[0]+10, accuracy[0], f'$k={neighbors[0]}$')
ax.text(speed[1], accuracy[1]-0.7, f'$k={neighbors[1]}$')
ax.text(speed[2]+4, accuracy[2]-1., f'$k={neighbors[2]}$', horizontalalignment='right')
#ax.set_ylim(86, 93)

# baselines = [
#     (104, 54.2, '2D CNN baseline'),
#     (185, 62.1, 'DSv1 CNN variant'),
#     (185, 83.8, 'DSv1 FCN variant'),
# ]
# for x, y, label in baselines:
#     ax.scatter(x, y, c=(1, 0, 0), marker='x')
#     ax.text(x, y+0.5, label, horizontalalignment='left')

fig.tight_layout()
filename = path.splitext(path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
