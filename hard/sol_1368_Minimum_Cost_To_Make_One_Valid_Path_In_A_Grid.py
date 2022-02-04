import heapq
import collections
from typing import List
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        moves = {1 : [0,1], 2 : [0,-1], 3 : [1,0], 4:[-1,0]}
        m = len(grid)
        n = len(grid[0])
        visited = set()
        h = []

        heapq.heappush(h, (0,0,0))
        visited.add((0,0,0))


        while h:

            cost,x,y = heapq.heappop(h)
            if x == m - 1 and y == n-1:
                return cost

            for move in moves:
                dx,dy = moves[move]
                next_x, next_y = x + dx, y + dy
                if not (0 <= next_x <m) or not (0 <= next_y < n):
                    continue


                if move == grid[x][y] and (cost, next_x,next_y) not in visited:
                    heapq.heappush(h,(cost,next_x,next_y))
                    visited.add((cost , next_x, next_y))

                elif (cost, next_x,next_y) not in visited:
                    heapq.heappush(h,(cost + 1,next_x,next_y))
                    visited.add((cost + 1,next_x, next_y))


        return cost





if __name__ == '__main__':
    print(Solution().minCost(grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
    print(Solution().minCost(grid = [[1,1,3],[3,2,2],[1,1,4]]))
