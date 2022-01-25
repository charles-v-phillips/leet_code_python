import heapq
class Solution:
    def findShortestWay(self, maze, ball, hole):
        moves = {'d':[1, 0],'r': [0, 1],'u' :  [-1, 0],'l': [0, -1]}
        m = len(maze)
        n = len(maze[0])
        dist_to = [[[float('inf'),'']] * n for _ in range(m)]
        dist_to[ball[0]][ball[1]] = [0,'']

        def get_next_moves(pos):
            next_moves = []
            for  direction,v in moves.items():
                dx,dy = v
                x, y, distance,tm = pos
                distance = 0
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                    x = x + dx
                    y = y + dy

                    distance += 1
                    if [x, y] == hole:
                        next_moves.append([x, y, distance, tm + direction])

                if [x, y] != pos[:2]:
                    next_moves.append([x, y, distance,tm + direction])

            return next_moves

        def relax(pos):
            next_moves = get_next_moves(pos)
            for next_pos in next_moves:

                if dist_to[next_pos[0]][next_pos[1]][0] >= dist_to[pos[0]][pos[1]][0] + next_pos[2]:
                    if [next_pos[0],next_pos[1]] == hole and dist_to[next_pos[0]][next_pos[1]][1]!= '':
                        new_path = min(dist_to[next_pos[0]][next_pos[1]][1],next_pos[3])
                    else:
                        new_path = next_pos[3]


                    dist_to[next_pos[0]][next_pos[1]] = [dist_to[pos[0]][pos[1]][0] + next_pos[2],new_path]
                    heapq.heappush(h,(dist_to[next_pos[0]][next_pos[1]][0],next_pos))

        ball.append(0)
        ball.append('')
        h = []
        heapq.heappush(h,(0,ball))
        get_next_moves(ball)
        while h:
            pos = heapq.heappop(h)
            relax(pos[1])
        if dist_to[hole[0]][hole[1]][0] != float('inf'):
            return dist_to[hole[0]][hole[1]][1]

        return 'impossible'


if __name__ == '__main__':
    print(Solution().findShortestWay([[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]],
[0,4],
[3,5]))