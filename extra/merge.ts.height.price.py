import json
import time
import datetime

ts_to_price = {}

prices = json.load(open("coindesk.txt"))
for key, value in prices['bpi'].items():
    ts = time.mktime(datetime.datetime.strptime(key, "%Y-%m-%d").timetuple())
    ts_to_price[ts] = value

gap = 144 * 7

def find_average_price(ts_start, ts_end, ts_to_price):
    sum = 0
    count = 0
    for ts, price in ts_to_price.items():
        if ts >= ts_start and ts <= ts_end:
            sum += price
            count += 1

    return sum * 1.0/count if count > 0 else 0


height_to_price = {}

ts_start = 0
for line in open('ts.to.height.csv', 'r').readlines():
    ts, height = map(int, line.split(','))
    if height % gap == 0:
        height_to_price[height] = find_average_price(ts_start, ts, ts_to_price)
        ts_start = ts

for height, price in height_to_price.items():
    print(','.join([str(height), str(price)]))
