from stuff import *
import time
import math
class Solution:
    def numTrees(self, n: int) -> int:
        d = {}
        def count_trees(lower,upper):
            if lower >= upper: return 1
            if (lower,upper) in d:return d[(lower,upper)]

            num = 0
            for i in range(lower,upper+1):
                numL = count_trees(lower, i - 1)
                numR = count_trees(i+1, upper)
                num += numL*numR
            d[(lower,upper)] = num
            return num

        return count_trees(1,n)




if __name__ == '__main__':
    s = Solution()
    t = time.time()
    print(s.numTrees(19))
    print("{} ms".format(time.time() - t))
