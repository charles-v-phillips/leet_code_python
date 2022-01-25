import heapq
from collections import Counter

class Solution:
    def reorganizeString(self,s):
        counter = Counter(s)
        h = []
        for k, v in counter.items():
            heapq.heappush(h,(-v,k))

        l = []

        n, letter = heapq.heappop(h)
        n = abs(n)
        for i in range(n):
            l[2*i] = letter

        while h:
            n, letter = heapq.heappop(h)
            n = abs(n)












if __name__ == '__main__':
    Solution().reorganizeString('aab')


