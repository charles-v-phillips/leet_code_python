from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = r = 0
        tot = nums[r]
        num_sub_arrays = 0
        while r < len(nums) and l <= r:
            if tot == k:
                num_sub_arrays += 1
                tot -= nums[l]
                l += 1
                r +=1
                if r < len(nums):
                    tot += nums[r]

            elif tot < k:
                r += 1
                if r < len(nums):
                    tot += nums[r]
            elif tot > k:
                tot -= nums[l]
                l += 1

        return num_sub_arrays

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i,n):
        #         s = sum(nums[i:j + 1])
        #         if s == k:
        #             count += 1
        #
        # return count
        count = 0
        n = len(nums)
        dp = [0] * (n + 1)

        dp[0] = 0
        for i in range(1,n + 1):
            dp[i] = dp[i-1] + nums[i-1]
        for i in range(n):
            for j in range(i + 1 ,n + 1):
                if dp[j] - dp[i] == k:
                    count += 1
        return count

from collections import defaultdict
class Solution3:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        running_sum = 0
        count = 0
        for e in nums:
            running_sum += e

            if running_sum == k:
                count += 1

            count += d[running_sum - k]
            d[running_sum] += 1
        return count













if __name__ == '__main__':
    print(Solution3().subarraySum(nums = [1,1,1], k = 2))
