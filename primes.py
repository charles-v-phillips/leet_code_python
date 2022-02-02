from itertools import combinations

# function to find all primes within range [l, h)
def find_primes(l,h):
    candidates = list(range(h))
    for i in range(2,len(candidates)):
        if candidates[i] == 0:
            continue
        t = i+i
        while t < len(candidates):
            candidates[t] = 0
            t = t+i
    return [e for e in candidates if e >= l]




#function that returns a tuple of the digits of a number in sorted order. Ex : 5324 -> (2,3,4,5)
def generate_key(num):
    digits = []
    while num:
        num,d = divmod(num,10)
        digits.append(d)
    return tuple(sorted(digits))


from collections import defaultdict
def find_prime_permutations_dict(primes):
    d = defaultdict(list)
    for p in primes:
        d[generate_key(p)].append(p)
    return d


def same(l):
    f = l[0]
    for e in l:
        if f != e:
            return False
    return True


def is_arithmetic(l):
    differences = [l[i] - l[i-1] for i in range(1,len(l))]
    return same(differences)





def solve():
    rv = []
    four_dig_primes = find_primes(1000,10000)
    digit_perms_dict = find_prime_permutations_dict(four_dig_primes)
    for v in digit_perms_dict.values():
        combos = combinations(v,3)
        for combo in combos:
            if is_arithmetic(combo):
                rv.append(combo)
    return rv



print(solve())