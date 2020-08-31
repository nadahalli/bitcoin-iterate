import pylab as plt
import pickle
from collections import defaultdict

gap = 144 * 7

X = pickle.load(open("labels.pkl", "rb"))
Y = pickle.load(open("values.pkl", "rb"))
block_to_price = {}
for line in open('label.to.price.csv', 'r').readlines():
    block, price = line.split(',')
    block_to_price[int(block)] = float(price)

spents = []
unspents = []
prices = []
heights = []

for height, spent_index in enumerate(X):
    spent = 0
    unspent = 0
    for j, y in enumerate(Y):
        if j == 0:
            unspent += y[height]
        else:
            spent += y[height]
    spents.append(spent)
    unspents.append(unspent)
    prices.append(block_to_price.get(height * gap))
    heights.append(height * gap)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Height')
ax1.set_ylabel('UTXOs', color=color)
ax1.plot(heights, spents, color=color)
#ax1.plot(heights, unspents, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('price in usd', color=color)  # we already handled the x-label with ax1
ax2.plot(heights, prices, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

    
