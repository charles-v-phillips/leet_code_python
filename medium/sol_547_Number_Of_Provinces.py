class Solution:
    def findCircleNum( isConnected):
        n = len(isConnected)
        visited = [False] * n

        def dfs(r):
            visited[r] = True
            for i in range(n):
                if isConnected[r][i] and not visited[i]:
                    dfs(i)
        numC = 0
        for i in range(n):
            if not visited[i]:
                numC += 1
                dfs(i)

        return numC
if __name__ == '__main__':
    print(Solution.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))
