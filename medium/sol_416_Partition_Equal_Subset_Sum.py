from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def helper(i, sum_added, sum_left_out):
            if i == n:
                return sum_added == sum_left_out
            if (i,sum_added, sum_left_out) in memo:
                return memo[(i,sum_added, sum_left_out)]

            splittable = helper(i + 1, sum_added + nums[i], sum_left_out) or helper(i + 1, sum_added, sum_left_out + nums[i])

            memo[(i, sum_added, sum_left_out)] = splittable
            return splittable
        return helper(0,0,0)


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        tot_sum = sum(nums)
        if tot_sum % 2 == 1:
            return False

        target = tot_sum//2

        dp = set()
        dp.add(0)


        for i in range(n):
            nextDP = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP

        return True if target in dp else False




if __name__ == '__main__':
    print(Solution2().canPartition(nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))

