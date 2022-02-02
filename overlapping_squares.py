from random import uniform
def play():
    x1,y1,x2,y2 = uniform(0,83),uniform(0,83),uniform(0,83),uniform(0,83)
    return  abs(x1 - x2) <=17 and abs(y2 - y1) <= 17

def sim(n = 10_000_00):
    cnt = 0
    for i in range(n):

        if play():
            cnt +=1
        if i % 1000 == 0:
         print(i)
    return cnt/n

print(sim())

