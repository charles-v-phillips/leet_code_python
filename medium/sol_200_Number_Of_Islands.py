class Solution:
    def numIslands(grid):
        m = len(grid)
        n = len(grid[0])
        moves = [(1,0),(0,1),(-1,0), (0,-1)]
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y):
            visited[x][y] = True

            for moveX, moveY in moves:
                nextX, nextY = x + moveX, y + moveY
                if 0 <= nextX < m and 0 <= nextY < n and grid[nextX][nextY] == '1' and not visited[nextX][nextY]:
                    dfs(nextX, nextY)


        num_components = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    num_components += 1
                    dfs(i,j)

        return num_components


if __name__ == '__main__':
    print(Solution.numIslands( grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))