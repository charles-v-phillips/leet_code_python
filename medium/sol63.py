class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0] ==1: return 0
        dp = [[-1]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]

        dp[0][0] = 1
        for i in range(1,len(dp[0])):
            dp[0][i] = 0 if obstacleGrid[0][i] == 1 or dp[0][i-1] == 0 else 1

        for i in range(1,len(dp)):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 or dp[i-1][0] == 0 else 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j]==0 else 0

        return dp[-1][-1]
if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))









