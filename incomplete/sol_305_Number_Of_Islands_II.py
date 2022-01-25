class QUF:
    def __init__(self,N):
        self.id = [i for i in range(N)]

    def root(self, i):
        while i != id[i]:
            i = id[i]
    def connected(self, p ,q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j




class Solution:
    def numIslands2( m, n, positions):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        quf = QUF(m*n)
        def get_possible_connections(x, y):
            possible_moves = []
            for dx , dy in moves:
                nextX = x + dx
                nextY = y + dy
                if 0 <= nextX < m and 0 <= nextY < n:
                    possible_moves.append((nextX,nextY))



        def foo(i,j):
            return i*n + j
        mapping = [foo(x,y) for x, y in positions]
        print(mapping)











if __name__ == '__main__':
    Solution.numIslands2(m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]])