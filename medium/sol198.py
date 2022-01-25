class Solution:
    def rob(self, nums) -> int:
        # memo = [-1 for _ in range(len(nums))]

        def dfs(pos):
            if pos >= len(nums)-2:
                return nums[pos]
            # if memo[pos] != -1:
            #     return memo[pos]

            max_profit = nums[pos] + max([dfs(i) for i in range(pos+2,len(nums))])
            # memo[pos] = max_profit
            return max_profit

        if len(nums) <=2:
            return max(nums)


        return max(dfs(0),dfs(1))

class Solution2:
    def rob(self, nums):
        if len(nums) <=2:
            return max(nums)

        started_1 = [0 for _ in range(len(nums)+1)]
        started_2 = [0 for _ in range(len(nums) + 1)]

        #padding
        started_1[0] = 0
        started_1[1] = nums[0]
        started_2[0] = 0
        started_2[1] = 0

        for i in range(2,len(nums)+1):
            started_1[i] = max(started_1[i-1],started_1[i-2] + nums[i-1])
            started_2[i] = max(started_2[i-1],started_2[i-2] + nums[i-1])

        return max(started_1[i],started_2[i])





class Solution3:
    def rob(self,arr):
        n = len(arr)
        dp = [0]*n
        dp[0] = arr[0]
        dp[1] = arr[1]

        for i in range(2, n):
            dp[i] = max(dp[i-1],dp[i-2] + arr[i])

        return dp[-1]






if __name__ == '__main__':
    arr = [1,2,3,1]
    s = Solution3()
    print(s.rob(arr))
    # print(s.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))