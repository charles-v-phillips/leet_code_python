# DFS, pretty slow, only beats 20 percent of submissions
class Solution:

    def has_path(self, maze, start, destination):
        moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(maze)
        n = len(maze[0])
        visited = [[False] * n for _ in range(m)]

        def get_next_moves(pos):
            next_moves = []
            for dx, dy in moves:
                x, y = pos
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                    x = x + dx
                    y = y + dy

                if [x, y] != pos:
                    next_moves.append([x, y])
            return next_moves

        def helper(pos):
            if pos == destination:
                return True
            if visited[pos[0]][pos[1]]:
                return False

            visited[pos[0]][pos[1]] = True

            for nextX, nextY in get_next_moves(pos):
                if helper([nextX, nextY]):
                    return True

            visited[pos[0]][pos[1]] = True
            return False

        return helper(start)


from collections import deque


class Solution2:
    def has_path(self, maze, start, destination):
        moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(maze)
        n = len(maze[0])
        visited = [[False] * n for _ in range(m)]

        def get_next_moves(pos):
            next_moves = []
            for dx, dy in moves:
                x, y = pos
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                    x = x + dx
                    y = y + dy

                if [x, y] != pos:
                    next_moves.append([x, y])
            return next_moves

        q = deque()
        q.append(start)
        visited[start[0]][start[1]] == True

        while q:
            pos = q.popleft()
            if pos == destination:
                return True
            for next_pos in get_next_moves(pos):
                if not visited[next_pos[0]][next_pos[1]]:
                    visited[next_pos[0]][next_pos[1]] = True
                    q.append(next_pos)
        return False


if __name__ == '__main__':
    print(
        Solution2().has_path(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                             start=[0, 4],
                             destination=[4, 4]))

    print(
        Solution2().has_path(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                             start=[0, 4],
                             destination=[3, 2]))
    print(
        Solution2().has_path(maze=[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],
                             start=[4, 3],
                             destination=[0, 1]))
