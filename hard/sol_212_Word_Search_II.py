class Trie:
    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        t = self.children
        for c in word:
            if c in t:
                t = t[c]
            else:
                t[c] = {}
                t = t[c]
        t['*'] = '*'

    def search(self, word: str) -> bool:
        t = self.children
        for c in word:
            if c in t:
                t = t[c]
            else:
                return False
        return '*' in t


    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        t = self.children
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


class Solution:
    def findWords(self, board, words):
        moves = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y, partial,d):
            if '*' in d:
                rv.add(partial)

            visited[x][y] = True

            for dx, dy in moves:
                nextX = x + dx
                nextY = y + dy
                if 0 <= nextX < m and 0 <= nextY < n and not visited[nextX][nextY] and board[nextX][nextY] in d:
                    dfs(nextX,nextY,partial + board[nextX][nextY], d[board[nextX][nextY]])

            visited[x][y] = False




        trie = Trie()
        for word in words:
            trie.insert(word)
        rv = set()

        for c in trie.children:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == c:
                        dfs(i,j,c,trie.children[c])
        return list(rv)


if __name__ == '__main__':
    print(Solution().findWords(board = [["a"]],
                               words = ["a"]))