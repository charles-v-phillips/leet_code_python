from typing import List
from collections import deque
class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = max_len = 0
        zeros = deque()
        while r < len(nums):
            if nums[r] == 0 and len(zeros) < k:
                zeros.append(r)

            elif nums[r] == 0 and  len(zeros)  == k:
                zeros.append(r)
                l = zeros.popleft() + 1

            else:
                pass
            r += 1
            max_len = max(max_len, r - l)
        return max_len

if __name__ == '__main__':
    print(Solution().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))

