import sys
import pylab as plt
import pickle
from collections import defaultdict

X = pickle.load(open("labels.btc.pkl", "rb"))
Y = pickle.load(open("values.btc.pkl", "rb"))

nY = [Y[0]]
labels = [0]

fig, ax = plt.subplots()
ax.stackplot(X, *nY, labels=labels)
ax.legend(loc='upper left')
    
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

handles, labels = ax.get_legend_handles_labels()   #get the handles
ax.legend(reversed(handles), reversed(labels))

plt.show()
    
