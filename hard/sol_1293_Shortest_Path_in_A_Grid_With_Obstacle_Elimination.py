from typing import List
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = [[-1,0],[1,0],[0,1],[0,-1]]
        shortest_path = float('inf')
        visited = [[False] * n for _ in range(m)]

        def dfs(x,y,depth,passes):
            nonlocal shortest_path
            if x == m - 1 and y == n - 1:
                shortest_path = min(shortest_path, depth)
                return

            visited[x][y] = True

            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y]:
                    if grid[next_x][next_y] == 1 and passes > 0:
                        dfs(next_x, next_y, depth + 1, passes - 1)
                    elif grid[next_x][next_y] == 1 and passes == 0:
                        continue
                    else:
                        dfs(next_x, next_y, depth + 1, passes - 1)

            visited[x][y] = False

        dfs(0,0,0,k)
        return shortest_path if shortest_path != float('inf') else -1

from collections import deque
class Solution2:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        shortest_path = float('inf')
        visited = [[[False] * (k + 1) for _ in range(n)]  for _ in range(m)]
        visited[0][0][k] = True
        q = deque()
        q.append((0,0,0,k)) # x, y,dist_traveled,num_passes

        while q:
            x, y, depth, passes = q.popleft()
            if x == m-1 and y == n-1:

                shortest_path = min(shortest_path, depth)

            for dx, dy in moves:
                next_x, next_y = x + dx ,y + dy
                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y][passes]:
                    if grid[next_x][next_y] == 1 and passes > 0:
                        q.append((next_x, next_y, depth + 1, passes - 1))
                    elif grid[next_x][next_y] == 1 and passes == 0:
                        continue

                    else:
                        q.append((next_x, next_y, depth + 1, passes))

                    visited[next_x][next_y][passes] = True

        return shortest_path if shortest_path != float('inf') else -1






if __name__ == '__main__':
#     print(Solution2().shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1)) # 6
#     print(Solution2().shortestPath(grid = [[0, 1, 1], [1, 1, 1], [1, 0, 0]], k = 1)) # -1
#     print(Solution2().shortestPath(grid = [[0,0,0,0,0,0,0,0,0,0],
#                                           [0,1,1,1,1,1,1,1,1,0],
#                                           [0,1,0,0,0,0,0,0,0,0],
#                                           [0,1,0,1,1,1,1,1,1,1],
#                                           [0,1,0,0,0,0,0,0,0,0],
#                                           [0,1,1,1,1,1,1,1,1,0],
#                                           [0,1,0,0,0,0,0,0,0,0],
#                                           [0,1,0,1,1,1,1,1,1,1],
#                                           [0,1,0,1,1,1,1,0,0,0],
#                                           [0,1,0,0,0,0,0,0,1,0],
#                                           [0,1,1,1,1,1,1,0,1,0],
#                                           [0,0,0,0,0,0,0,0,1,0]],
#                                   k = 1)) # 20
#     print(Solution2().shortestPath(grid = [[0,0],
#                                            [1,0],
#                                            [1,0],
#                                            [1,0],
#                                            [1,0],
#                                            [1,0],
#                                            [0,0],
#                                            [0,1],
#                                            [0,1],
#                                            [0,1],
#                                            [0,0],
#                                            [1,0],
#                                            [1,0],
#                                            [0,0]],
#                                    k = 4
# ))
    print(Solution2().shortestPath([[0]], k = 1))











