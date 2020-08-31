import sys
import pylab as plt
import pickle
from collections import defaultdict

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--percentage',
                      type=eval, 
                      choices=[True, False], 
                      default='False')
parser.add_argument('--compress',
                      type=eval, 
                      choices=[True, False], 
                      default='False')

args = parser.parse_args()

X = pickle.load(open("labels.btc.pkl", "rb"))
Y = pickle.load(open("values.btc.pkl", "rb"))
max_labels = 20
gap = 1024

pY = defaultdict(list)

for i, x in enumerate(X):
    sum = 0
    sum_compress = 0
    for j, y in enumerate(Y):
        if args.compress:
            if j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                sum_compress += y[i]/(gap/pow(2, j))
                sum += y[i]/(gap/pow(2, j))
            else:
                sum += y[i]

        else:
            sum += y[i]

    compression_done = False
    for j, y in enumerate(Y):
        to_add = y[i]
        if args.compress:
            if j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                if not compression_done:
                    to_add = sum_compress
                    compression_done = True
                    if args.percentage:
                        pY[j].append(100.0 * to_add/sum)
                    else:
                        pY[j].append(to_add)
            else:
                if args.percentage:
                    pY[j].append(100.0 * to_add/sum)
                else:
                    pY[j].append(to_add)

        else:
            if args.percentage:
                pY[j].append(100.0 * to_add/sum)
            else:
                pY[j].append(to_add)

for key, value in pY.items():
    print(key, len(value))

nY = []
labels = []
nY.append(pY[0])
labels.append(0)
for key, value in sorted(pY.items(), reverse=True):
    if key == 0:
        continue
    nY.append(value)
    labels.append(key)
    

fig, ax = plt.subplots()
ax.stackplot(X, *nY, labels=labels)
ax.legend(loc='upper left')
    
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

handles, labels = ax.get_legend_handles_labels()   #get the handles
ax.legend(reversed(handles), reversed(labels))

plt.show()
    
