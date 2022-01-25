import math
def decimals(num):
    r = 10
    while r != 0:
        q,r = divmod(r,num)
        yield(q)

        r*=10


def genlimit(g, limit):
    l = zip(range(limit), g)
    for x, y in l:
        yield y

def decimals2(num):
    l = []
    r = 10
    while r != 0:
        q,r = divmod(r,num)
        if q in l:
            start = l.index(q)
            non_rep = l[:start]
            rep = l[start:]
            yield (non_rep,rep)
            return
        l.append(q)
        yield(q)
        r*=10

if __name__ == '__main__':
    print(list(decimals2(7)))




