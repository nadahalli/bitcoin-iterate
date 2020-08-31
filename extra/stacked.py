import numpy as np
import pylab as plt
import math
from collections import defaultdict
import sys
import time

gap = 1024
max_labels = 20

X = []
Ys = defaultdict(list)
gap_ys = defaultdict(int)

def mylog(x):
    return math.floor(math.log(x, 2))

new_chunk = True

for line in sys.stdin:
    block, life, amount, coinbase = map(int, line.split(','))
    amount = amount / 10000000
    if block % gap == 0 and new_chunk:
        new_chunk = False
        for label in range(0, max_labels):
            Ys[label].append(gap_ys.get(label, 0))
        gap_ys.clear()
        X.append(block - gap)
        print(time.asctime(), block - gap)
    if block % gap != 0:
        new_chunk = True

    label = mylog(life + 2)
    gap_ys[label] += amount

for key, value in sorted(Ys.items()):
    print(key, len(value))

Y = []
for key, value in sorted(Ys.items()):
    Y.append(value)

import pickle

with open('labels.btc.pkl', 'wb') as f:
    pickle.dump(X, f)
with open('values.btc.pkl', 'wb') as f:
    pickle.dump(Y, f)    

fig, ax = plt.subplots()
ax.stackplot(X, *Y, labels=[i for i in range(0, max_labels)])
ax.legend(loc='upper left')
    
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
