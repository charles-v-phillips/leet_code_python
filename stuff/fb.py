import pandas as pd
import numpy as np
d = {'fbid' : [1,2,3,4], 'action' : [1001,981,734,985], 'type' : ['post','comment','photo','share'],
     'referredid' : [345, 1001,234,1001]}

transactions = pd.DataFrame(d).T.to_dict()


d = {}
print(transactions)
for t in transactions:
    if transactions[t]['referredid'] in d and transactions[t]['type'] == 'comment':
        d[transactions[t]['referredid']] += 1
    else:
        d[transactions[t]['action']] = 0
print(d)
print('\n\n\n')

count = {}

for e in d.values():
    if e in count:
        count[e] +=1
    else:
        count[e] = 1
print(count)



if __name__ == '__main__':
    pass