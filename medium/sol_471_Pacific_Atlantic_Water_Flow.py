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



class Solution2:
    def pacificAtlantic(self, heights):
        p = set()
        a = set()
        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            p.add((i, 0))
            a.add((i, n-1))

        for i in range(n):
            p.add((0, i))
            a.add((m-1, i))



        reachable_from_atlantic = set()
        reachable_from_pacific = set()

        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y, s):
            s.add((x,y))
            for dx, dy in moves:
                next_x = x + dx
                next_y = y + dy
                if 0 <= next_x < m and 0 <= next_y < n and (next_x, next_y) not in s\
                        and heights[x][y] <= heights[next_x][next_y]:
                    dfs(next_x, next_y, s)


        for x, y in p:
            dfs(x, y, reachable_from_pacific)
        for x, y in a:
            dfs(x, y, reachable_from_atlantic)
        return list(reachable_from_pacific.intersection(reachable_from_atlantic))





if __name__ == '__main__':
    print(Solution2().pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    # print(Solution2().pacificAtlantic(heights = [[2,1],[1,2]])) # [[0,0],[0,1],[1,0],[1,1]]