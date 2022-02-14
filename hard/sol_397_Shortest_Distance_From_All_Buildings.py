from typing import List
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = [[1,0],[-1,0],[0,-1],[0,1]]
        moves_to = [[[0,0] for _ in range(n)] for _ in range(m)]
        def get_building_locations_and_open_spots():
            buildings = []
            open_spots = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        buildings.append([i,j])
                    if grid[i][j] == 0:
                        open_spots += 1

            return buildings, open_spots

        def bfs(x,y):
            visited = set()
            q = deque()
            q.append((x,y,0))
            visited.add((x,y))


            while q:
                x,y,distance = q.popleft()
                moves_to[x][y][0] += distance

                for dx, dy in moves:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < m and 0 <= next_y < n and (next_x,next_y) not in visited and grid[next_x][next_y] == 0:
                        q.append((next_x,next_y,distance + 1))
                        moves_to[next_x][next_y][1] += 1
                        visited.add((next_x, next_y))




        buildings, open_spots = get_building_locations_and_open_spots()
        # if not open_spots:
        #     return -1
        for i,j in buildings:
            bfs(i,j)


        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and moves_to[i][j][1] == len(buildings):
                    min_dist = min(min_dist,moves_to[i][j][0])

        return min_dist if min_dist != float('inf') else -1








if __name__ == '__main__':
    print(Solution().shortestDistance(grid = [[1,0,2,0,1],
                                              [0,0,0,0,0],
                                              [0,0,1,0,0]]))
    print(Solution().shortestDistance(grid = [[1]]))
    print(Solution().shortestDistance([[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]]))
    print(Solution().shortestDistance([[1,0]]))
    print(Solution().shortestDistance([[1,2,0]]))
    print(Solution().shortestDistance([[0, 2, 0, 2, 2, 0, 2, 2],
                                       [0, 2, 2, 2, 1, 0, 1, 2],
                                       [0, 0, 0, 1, 0, 2, 0, 0],
                                       [2, 0, 0, 2, 0, 2, 2, 0],
                                       [0, 0, 0, 2, 0, 0, 0, 0]]))

