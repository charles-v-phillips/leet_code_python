class Solution:
    def uniquePathsIII(self, grid) -> int:
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        numSteps, startX, startY, endX, endY = 0,0,0,0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: startX, startY = i,j
                if grid[i][j] == 2: endX,endY = i,j
                if grid[i][j] == 0: numSteps +=1
        numSteps+=1 ##account for the end square
        def dfs(i,j,steps):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1 or visited[i][j] == True:
                return 0
            if i == endX and j == endY and steps == numSteps:
                return 1

            visited[i][j] = True

            num = dfs(i-1,j,steps+1) + dfs(i+1,j,steps+1) + dfs(i,j-1,steps+1) + dfs(i,j+1,steps+1)

            visited[i][j] = False

            return num


        return dfs(startX,startY,0)

if __name__ == '__main__':
    s = Solution()
    g = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    print(s.uniquePathsIII(g))