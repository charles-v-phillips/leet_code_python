class Solution:
    def exist(self, board, word: str):
        moves = [[1,0],[-1,0],[0,-1],[0,1]]
        m = len(board)
        n = len(board[0])
        str_len = len(word) - 1
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y, i):
            if i == str_len:
                return True
            visited[x][y] = True
            for dx, dy in moves:
                nextX = x + dx
                nextY = y + dy

                if 0 <= nextX < m and 0 <= nextY < n and not visited[nextX][nextY] and board[nextX][nextY] == word[i + 1]:
                    if dfs(nextX, nextY, i + 1):
                        return True

            visited[x][y] = False
            return False





        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))

