class Solution:


    def pacificAtlantic(self, heights):
        m = len(heights)
        n = len(heights[0])
        hit_atlantic = hit_pacific = False
        moves = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        visited = [[False] * n for _ in range(m)]

        def dfs(x,y):
            nonlocal hit_pacific
            nonlocal hit_atlantic
            if x == 0 or y == 0:
                hit_pacific = True

            if x == m-1 or y == n-1:
                hit_atlantic = True

            if hit_atlantic and hit_pacific:
                return True

            visited[x][y] = True
            for dx, dy in moves:
                nextX, nextY = x + dx, y + dy
                if 0 <= nextX < m and 0 <= nextY < n and not visited[nextX][nextY] and heights[nextX][nextY] <= heights[x][y]:

                    if dfs(nextX, nextY):
                        visited[x][y] = False
                        return True
            visited[x][y] = False
            return False

        rv = []
        for i in range(m):
            for j in range(n):
                dfs(i,j)
                if hit_pacific and hit_atlantic:
                    rv.append([i,j])
                hit_atlantic = hit_pacific = False
        return rv






if __name__ == '__main__':
    print(Solution().pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    print(Solution().pacificAtlantic(heights = [[2,1],[1,2]])) # [[0,0],[0,1],[1,0],[1,1]]