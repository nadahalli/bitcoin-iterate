import pylab as plt
import pickle
from collections import defaultdict

X = pickle.load(open("labels.pkl", "rb"))
Y = pickle.load(open("values.pkl", "rb"))
max_labels = 20

pY = defaultdict(list)

for i, x in enumerate(X):
    sum = 0
    for j, y in enumerate(Y):
        sum += y[i]
    for j, y in enumerate(Y):
        pY[j].append(100.0 * y[i]/sum)

nY = []
for key, value in sorted(pY.items()):
    nY.append(value)

fig, ax = plt.subplots()
ax.stackplot(X, *nY, labels=[i for i in range(0, max_labels)])
ax.legend(loc='upper left')
    
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
    
