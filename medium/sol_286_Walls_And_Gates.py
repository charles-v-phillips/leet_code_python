from typing import List
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        m = len(rooms)
        n = len(rooms[0])

        def bfs(r,c):
            visited = [[False] * n for _ in range(m)]
            q = deque()
            q.append([r,c])
            visited[r][c] = True
            dist_traveled = 0
            while q:
                num_nodes = len(q)
                dist_traveled += 1

                for i in range(num_nodes):
                    x,y = q.popleft()
                    for dx, dy in moves:
                        nextX, nextY = x + dx, y + dy

                        if 0 <= nextX < m and 0 <= nextY < n and rooms[nextX][nextY] != -1 and not visited[nextX][nextY] and rooms[nextX][nextY] != 0:
                            rooms[nextX][nextY] = min(rooms[nextX][nextY], dist_traveled)
                            visited[nextX][nextY] = True
                            q.append([nextX,nextY])



        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    bfs(i,j)


class Solution2:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i,j])


        while q :
            x,y = q.popleft()

            for dx, dy in moves:
                next_x = x + dx
                next_y = y + dy
                if 0 <= next_x < m and 0 <= next_y < n and rooms[next_x][next_y] > 2**30:
                    rooms[next_x][next_y] = rooms[x][y] + 1
                    q.append([next_x, next_y])












if __name__ == '__main__':
    Solution2().wallsAndGates(rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])







