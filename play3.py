import json
import numpy as np


def fib() -> int:
    f_0 = 1
    f_1 = 2
    sum = 1
    while True:
        f_next = f_0 + f_1
        f_0 = f_1
        f_1 = f_next

        if f_next < 4000000 and f_next %2 == 0:
            sum+=f_next
        if f_next > 4000000:
            return sum


d = {
    'staten_island' : range(120,124),
    'queens' : range(100,116),
    'brooklyn' : range(60,95),
    'bronx' : range(40,53),
    'manhattan' : range(1,35)
}


def j():
    with open('/Users/charlesphillips/nycdsa/projects/project2/data/precincts-2.json') as f:
        data = json.load(f)
        print("HI")
        for e in data['features']:
            if e['properties']['Precinct'] == 1:
                print("FOUND")



def f():
    with open('/Users/charlesphillips/nycdsa/projects/project2/geo_jsons/precincts-2.json') as f:
        data = json.load(f)
        for k in d.keys():
            dic = {}
            dic['type'] = 'FeatureCollection'
            dic['features'] = []
            for e in data['features']:
                n = e['properties']['Precinct']
                if n in d[k]:
                    print(f'{k} : {n}')
                    dic['features'].append(e)
            with open(f'{k}_precincts.json','w') as f:
                json.dump(dic,f)



if __name__ == '__main__':
    f()
