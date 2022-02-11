from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def helper(i ,arr):
            if i == n:
                return 1 if sum(arr) == target else 0
            solutions = 0

            solutions += helper(i + 1, arr)
            arr[i] = -arr[i]
            solutions += helper(i + 1, arr)
            arr[i] = -arr[i]
            return solutions

        return helper(0,nums)

class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def helper(i, tot):
            if i == n:
                return 1 if tot == target else 0
            if (i, tot) in memo:
                return memo[(i,tot)]

            memo[(i,tot)] = helper(i + 1, tot + nums[i]) + helper(i + 1, tot - nums[i])



            return memo[(i, tot)]

        return helper(0,0)





if __name__ == '__main__':
    print(Solution2().findTargetSumWays([1, 1, 1, 1, 1, 3, 1, 4, 2, 7, 1, 2, 1, 1, 4, 3, 7, 4, 1, 1, 5, 7,1], 3))
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1, 3, 1, 4, 2, 7, 1, 2, 1, 1, 4, 3, 7, 4, 1, 1, 5, 7,1], 3))
