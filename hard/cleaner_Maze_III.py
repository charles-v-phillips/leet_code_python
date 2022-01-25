class Tile:
    def __init__(self, distance_to = 0, path_to = ''):
        self.distance_to = distance_to
        self.path_to = path_to

    def __str__(self):
        return f'd: {self.distance_to} p: {self.path_to}'

    def __repr__(self):
        return self.__str__()

class Move:
    def __init__(self,x,y,distance_traveled, path_to):
        self.x = x
        self.y = y
        self.distance_traveled = distance_traveled
        self.path_to = path_to
    def __str__(self):
        return f'x: {self.x}  y: {self.y} dt: {self.distance_traveled} pt: {self.path_to}'
    def __repr__(self):
        return self.__str__()

import pprint
import heapq
class Solution:
    def findShortestWay(self, maze, ball, hole):
        moves = {'d': [1, 0], 'r': [0, 1], 'u': [-1, 0], 'l': [0, -1]}
        m = len(maze)
        n = len(maze[0])
        dist_to = [[Tile()] * n for _ in range(m)]
        def get_next_moves(pos):
            next_moves = []
            for  direction,v in moves.items():
                dx,dy = v
                x, y, distance,tm = pos.x, pos.y, pos.distance_traveled, pos.path_to
                distance = 0
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                    x = x + dx
                    y = y + dy

                    distance += 1
                    if [x, y] == hole:
                        next_moves.append(Move(x, y, distance, tm + direction))

                if [x, y] != [pos.x, pos.y]:
                    next_moves.append(Move(x, y, distance,tm + direction))

            return next_moves
        def relax(pos):
            next_moves = get_next_moves(pos)
            for next_pos in next_moves:

                if dist_to[next_pos.x][next_pos.y].distance_to > dist_to[pos.x][pos.y].distance_to + next_pos.distance_traveled:
                    dist_to[next_pos.x][next_pos.y].distance_to = dist_to[pos.x][pos.y].distance_to + next_pos[2]
                    dist_to[next_pos.x][next_pos.y].path_to = next_pos[3]

                    # if next_pos == hole:
                    #     dist_to[next_pos[0]][next_pos[1]][1] = min()
                    heapq.heappush(h,(dist_to[next_pos.x][next_pos.y][0],next_pos))

        h = []
        start = Move(ball[0],ball[1],0,'')
        heapq.heappush(h, (0, start))
        while h:
            pos = heapq.heappop(h)
            relax(pos[1])
        if dist_to[hole[0]][hole[1]] != float('inf'):
            return dist_to[hole[0]][hole[1]].path_to

        return -1

if __name__ == '__main__':
    print(Solution().findShortestWay(maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],
                                   ball = [4,3],
                                   hole = [0,1]))