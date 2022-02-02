from typing import List
from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        h = []
        for i in range(k):
            d.append(nums[i])
            heapq.heappush(h,-nums[i])

        rv = []
        rv.append(-h[0])

        for i in range(k,len(nums)):
            take_off = d.popleft()
            d.append(nums[i])
            if take_off == -h[0]:
                heapq.heappop(h)
            heapq.heappush(h, -nums[i])
            rv.append(-h[0])
        return rv

from collections import defaultdict
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        deq = deque()
        h = []
        for i in range(k):
            dic[nums[i]] += 1
            deq.append(nums[i])
            if dic[nums[i]] == 1:
                heapq.heappush(h,-nums[i])
        rv = []
        rv.append(-h[0])

        for i in range(k,len(nums)):
            takeoff = deq.popleft()
            dic[takeoff] -= 1
            deq.append(nums[i])
            dic[nums[i]] += 1
            if takeoff == -h[0] and dic[takeoff] == 0:
                heapq.heappop(h)
            if dic[nums[i]] == 1:
                heapq.heappush(h,-nums[i])
            rv.append(-h[0])
        return rv


class Solution3:
    def maxSlidingWindow(self,nums, k):
        q = deque()
        rv = []
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                rv.append(nums[q[0]])
                l += 1
            r += 1
        return rv





if __name__ == '__main__':
    print(Solution3().maxSlidingWindow([9,10,9,-7,-4,-8,2,-6],5))