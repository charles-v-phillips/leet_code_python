import math
from typing import List
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def isPrime(n):
            if n <2: return False
            if n == 2: return True
            if n % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(n)) + 1, 2 ):
                if n % i == 0:
                    return False
            return True

        rv = []
        def helper(n,factors,prev):
            if isPrime(n):
                rv.append(factors + [n])
                return


            for i in range(2,prev):
                if n % i == 0:
                    helper(n//i, factors + [i],n//i)

        if isPrime(n):
            return rv
        helper(n,[],n)
        return rv


class Solution2:
    def getFactors(self, n):
        rv = []
        if n == 1:
            return rv

        def dfs(path=[], rest=2, target=n):
            if len(path) > 0:
                rv.append(path + [target])

            for i in range(rest, int(math.sqrt(target)) + 1):
                if target % i == 0:
                    dfs(path + [i], i, target // i)

        dfs()
        return rv






if __name__ == '__main__':
    print(Solution2().getFactors(32))