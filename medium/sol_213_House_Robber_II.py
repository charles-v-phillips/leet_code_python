class Solution:
    def rob(self, nums) -> int:
        n = len(nums)

        dp0 =  [0] * n
        dp1 = [0] * n
        dp0[0] = dp0[1] = nums[0]
        dp1[1] = nums[1]

        for i in range(2, n):
            dp0[i] = max(dp0[i - 2] + nums[i], dp0[i - 1])
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        return max(dp0[-2], dp1[-1])

if __name__ == '__main__':
    print(Solution().rob([4,1,2,7,5,3,1]))