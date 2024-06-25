# dollar = 83.56 * rs

prices_in_dollars = {'apple': 2.5, 'banana': 1.8, 'orange': 3.0}

prices_in_rs = dict(map(lambda mon : (mon[0],round((mon[1]*83.56),2)),prices_in_dollars.items()))

print(prices_in_rs)