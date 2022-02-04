from itertools import permutations


def has_357_only(num):
        s = set(['3','5','7'])
        return set(str(num)) == s
def sum_digs_divis_by_357(num):
        tot = sum(int(c) for c in str(num))
        return tot % 105 == 0

def divis_by_357(num):
        return num % 105




def tuple_to_int(tup):
        s = ''
        for c in tup:
                s += c
        return int(s)

from collections import deque
start = deque(tuple_to_int(t) for t in permutations('357'))
seen = set([357])

print(start)


num = 33577577777777775

print(divis_by_357(num) and sum_digs_divis_by_357(num))
while start:
        num = start.popleft()
        print(num)
        if sum_digs_divis_by_357(num) and divis_by_357(num):
                print(f'FOUND NUM : {num}')
                break

        for digit in ['3','5','7']:
                next_perms = list(permutations(str(num) + digit))
                for np in next_perms:
                        next_num = tuple_to_int(np)
                        if next_num not in seen:
                                start.append(next_num)
                                seen.add(next_num)








