class Solution:
    def uniquePathsIII(self, grid) -> int:
        n = len(grid[0])
        m = len(grid)
        visited = [[False] * n for _ in  range(m)]
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        num_obstacles = -sum(grid[i][j] for i in range(m) for j in range(n) if grid[i][j] == -1)
        num_open_spots = m*n - num_obstacles
        def dfs(x,y,depth):
            if depth == num_open_spots and grid[x][y] == 2:
                return 1
            if grid[x][y] == 2:
                return 0

            visited[x][y] = True
            val = sum(dfs(x + dx, y + dy, depth + 1) for dx,dy in moves if 0 <= x + dx < m and 0 <= y + dy < n and grid[x +dx][y + dy] != -1 and not visited[x + dx][y+dy])

            visited[x][y] = False
            return val

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i,j,1)



if __name__ == '__main__':
    # print(Solution().uniquePathsIII(grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
    # print(Solution().uniquePathsIII(grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]))

    t = (list(range(3)), [1,2,3], [7,8,9])
    t[2].append(4)
    print(t)

