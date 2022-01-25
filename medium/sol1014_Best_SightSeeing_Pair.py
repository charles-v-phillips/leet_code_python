class Solution:
    def maxScoreSightseeingPair(self, values) -> int:
        n = len(values)
        dp = [[0]*(n-1) for _ in range(n-1)]

        for i in range(n-1):
            dp[i][i] = values[i] +values[i+1] + 1

        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                pass
        print("H")

if __name__ == '__main__':
    print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))

