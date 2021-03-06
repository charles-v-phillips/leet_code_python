class Solution:
    def uniquePaths(self, m, n):
        def dfs(i, j):
            if i ==m-1 and j == n-1:
                return 1
            if i == m or j == n:
                return 0

            return  dfs(i+1,j) + dfs(i,j+1)

        def dp(m,n):
            dp = [[1]*n for _ in range(m)]

            for i in range(1,m):
                for j in range(1,n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[-1][-1]




        return dp(m,n)

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3,7))




