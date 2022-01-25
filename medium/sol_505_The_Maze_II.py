from collections import deque
# This solution fails on test case 68 /78 which is too big to debug. I dont know why s0 lets try dijkstra in Solution2
class Solution:
    def shortestDistance(self, maze, start, destination):
        moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(maze)
        n = len(maze[0])
        visited = [[False] * n for _ in range(m)]
        def get_next_moves(pos):
            next_moves = []
            for dx, dy in moves:
                x, y, distance = pos

                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                    x = x + dx
                    y = y + dy
                    distance += 1

                if [x, y] != pos[:2]:
                    next_moves.append([x, y, distance])
            return next_moves

        q = deque()
        start.append(0)
        q.append(start)
        visited[start[0]][start[1]] = True

        while q:
            pos = q.popleft()
            print(pos)
            if pos[:2] == destination:
                return pos[2]
            for next_pos in get_next_moves(pos):
                if not visited[next_pos[0]][next_pos[1]]:
                    visited[next_pos[0]][next_pos[1]] = True
                    q.append(next_pos)

        return -1

import heapq
class Solution2:
    def shortestDistance(self, maze, start, destination):
        moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(maze)
        n = len(maze[0])
        dist_to = [[float('inf')] * n for _ in range(m)]
        dist_to[start[0]][start[1]] = 0

        def get_next_moves(pos):
            next_moves = []
            for dx, dy in moves:
                x, y, distance = pos
                distance = 0
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                    x = x + dx
                    y = y + dy
                    distance += 1

                if [x, y] != pos[:2]:
                    next_moves.append([x, y, distance])
            return next_moves

        def relax(pos):
            for next_pos in get_next_moves(pos):
                if dist_to[next_pos[0]][next_pos[1]] > dist_to[pos[0]][pos[1]] + next_pos[2]:
                    dist_to[next_pos[0]][next_pos[1]] = dist_to[pos[0]][pos[1]] + next_pos[2]
                    heapq.heappush(h,(dist_to[next_pos[0]][next_pos[1]],next_pos))

        start.append(0)
        h = []
        heapq.heappush(h,(0,start))
        while h:
            pos = heapq.heappop(h)
            relax(pos[1])
        if dist_to[destination[0]][destination[1]] != float('inf'):
            return dist_to[destination[0]][destination[1]]
        return -1




if __name__ == '__main__':
    print(Solution2().shortestDistance(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
                                      start = [0,4],
                                      destination = [4,4]))