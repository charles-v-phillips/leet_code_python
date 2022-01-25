class Solution:

    def shortestPathBinaryMatrix(self, grid) -> int:
        def in_range(x,y):
            return x >=0 and y>=0 and x < self.n and y < self.n
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        if grid[0][0] == 1: return -1
        if len(grid) == 1: return 1 if grid[0][0] == 0 else -1
        self.n = len(grid)

        self.min_path = float('inf')
        visited = [[False]*self.n for _ in range(self.n)]

        def dfs(x,y,depth):
            if x == self.n-1 and y == self.n-1:
                self.min_path = min(self.min_path,depth)
                return
            visited[x][y] = True

            for move in self.moves:
                next_x  = x + move[0]
                next_y = y+ move[1]
                if in_range(next_x,next_y) and not visited[next_x][next_y] and grid[next_x][next_y] == 0:
                    dfs(next_x,next_y,depth + 1)

            visited[x][y] = False


        dfs(0,0,1)
        return self.min_path if self.min_path < float('inf') else -1

class Solution2:
    def shortestPathBinaryMatrix(self, grid) -> int:
        def in_range(x,y):
            return x >=0 and y>=0 and x < self.n and y < self.n
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        if grid[0][0] == 1: return -1
        if len(grid) == 1: return 1 if grid[0][0] == 0 else -1
        self.n = len(grid)

        self.min_path = float('inf')
        visited = [[False]*self.n for _ in range(self.n)]

        #BFS

        q = []
        q.append((0,0,1)) #startX, startY, depth
        visited[0][0] = True


        while q:
            node = q.pop(0)
            x = node[0]
            y = node[1]
            if x == self.n - 1 and y == self.n-1:
                return node[2]
            for move in self.moves:
                next_x = x + move[0]
                next_y = y + move[1]
                if in_range(next_x,next_y) and not visited[next_x][next_y] and grid[next_x][next_y] == 0:
                    q.append((next_x,next_y, node[2] + 1))
                    visited[next_x][next_y] = True

        return -1









if __name__ == '__main__':
    print(Solution2().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))








