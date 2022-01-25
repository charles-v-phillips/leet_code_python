class Solution:
    def deleteAndEarn(self, nums) -> int:
        nums = sorted(nums, reverse=True)
        points = 0

        i = 0
        while i < len(nums):
            points += nums[i]
            val = nums[i]
            while i < len(nums) and nums[i] >= val - 1:
                i += 1

        return points

from collections import Counter
class Solution2:
    def deleteAndEarn(self, nums):
        counter = Counter(nums)
        n = max(nums) + 1
        cash = [0]*n
        for i in range(n):
            cash[i] = counter[i]*i

        dp = [0]*n
        dp[0] = cash[0]
        dp[1] = cash[1]
        for i in range(2,n):
            dp[i] = max(dp[i-2] + cash[i], dp[i-1])
        return dp[-1]






if __name__ == '__main__':
    print(Solution2().deleteAndEarn([3,4,2]))
    print(Solution2().deleteAndEarn([2,2,3,3,3,4]))
