import numpy as np
import pylab as plt
import math
from collections import defaultdict
import sys
import time

max_block = 644276
gap = 144 * 7
max_labels = 20

X = []
Ys = defaultdict(list)
gap_ys = defaultdict(int)

for line in sys.stdin:
    block, life = map(int, line.split(','))
    if block % gap == 0 and new_block:
        new_block = False
        for label in range(0, max_labels):
            Ys[label].append(gap_ys.get(label, 0))
        gap_ys.clear()
        X.append(block - gap)
        print(time.asctime(), block - gap)
    if block % gap != 0:
        new_block = True

    bucket = math.floor(math.log(life + 2, 2))
    gap_ys[bucket] += 1

for key, value in sorted(Ys.items()):
    print(key, len(value))

Y = []
for key, value in sorted(Ys.items()):
    Y.append(value)

import pickle

with open('labels.pkl', 'wb') as f:
    pickle.dump(X, f)
with open('values.pkl', 'wb') as f:
    pickle.dump(Y, f)    

fig, ax = plt.subplots()
ax.stackplot(X, *Y, labels=[i for i in range(0, max_labels)])
ax.legend(loc='upper left')
    
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
