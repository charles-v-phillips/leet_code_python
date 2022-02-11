class Solution:
    def totalNQueens(self, n: int) -> int:
        occupied_horizontals = set()
        occupied_verticals = set()
        occupied_diagonals = set()
        occupied_anti_diagonals = set()
        board = [['.'] * n for _ in range(n)]

        def can_place(x, y):
            if x in occupied_horizontals:
                return False
            if y in occupied_verticals:
                return False

            diag = x - y
            if diag in occupied_diagonals:
                return False

            anti_diag = x + y
            if anti_diag in occupied_anti_diagonals:
                return False

            return True

        def place(x, y):
            occupied_horizontals.add(x)
            occupied_verticals.add(y)
            occupied_diagonals.add(x - y)
            occupied_anti_diagonals.add(y + x)

            board[x][y] = 'Q'

        def remove(x, y):
            occupied_horizontals.remove(x)
            occupied_verticals.remove(y)
            occupied_diagonals.remove(x - y)
            occupied_anti_diagonals.remove(y + x)

            board[x][y] = '.'

        def backtrack(k):
            if k == n:
                return 1

            solutions = 0
            for i in range(n):
                if can_place(k, i):
                    place(k, i)
                    solutions += backtrack(k + 1)
                    remove(k, i)
            return solutions

        return backtrack(0)




if __name__ == '__main__':
    print(Solution().totalNQueens(5))