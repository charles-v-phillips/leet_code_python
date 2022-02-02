from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = [[False] * n for _ in range(m)]
        memo = [[0] * n for _ in range(m)]
        max_path = 1
        def dfs(x, y, depth):
            nonlocal max_path
            visited[x][y] = True

            if memo[x][y]:
                return memo[x][y]

            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y]:
                    if matrix[x][y] < matrix[next_x][next_y]:
                        max_path = max(max_path, depth + 1)
                        dfs(next_x, next_y, depth + 1)
                    else:
                        max_path = max(max_path, depth)


            visited[x][y] = False





        for i in range(m):
            for j in range(n):
                dfs(i,j,1)

        return max_path

class Solution2:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[False] * n for _ in range(m)]
        memo = [[0] * n for _ in range(m)]


        def dfs(x,y):
            if visited[x][y]:
                return 0

            if memo[x][y]:
                return memo[x][y]

            visited[x][y] = True

            path_lengths = [1 + dfs(x + dx, y + dy) for dx, dy in moves if 0 <= x + dx < m and 0 <= y + dy < n and matrix[x][y] < matrix[x + dx][y  +dy]]
            path_lengths.append(0)
            max_len_path_from_here = max(path_lengths)

            memo[x][y] = max_len_path_from_here
            visited[x][y] = False
            return max_len_path_from_here


        return max(1 + dfs(i,j) for i in range(m) for j in range(n))





if __name__ == '__main__':
    print(Solution2().longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]]))
