class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        def helper(i):
            if i == len(cost) - 1:
                return cost[i]
            if i >=len(cost):
                return 0

            return cost[i] +min(helper(i+1),helper(i+2))
        return min(helper(0),helper(1))

class Solution2:
    def minCostClimbingStairs(self,cost):
        dp = [0]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(dp)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])

        return min(dp[-1],dp[-2])




if __name__ == '__main__':
    s = Solution2()
    print(s.minCostClimbingStairs([10,15,20]))
