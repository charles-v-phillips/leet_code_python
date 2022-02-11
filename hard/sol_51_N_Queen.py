from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        moves = [[1,0],[-1,0],[0,1],[0,-1], [1,1],[1,-1],[-1,1], [-1,-1]]
        def can_move(x,y):
            for dx, dy in moves:
                next_x, next_y = x,y
                while 0 <= next_x < n and 0 <= next_y < n :
                    if board[next_x][next_y] == 'Q':
                        return False
                    next_x += dx
                    next_y += dy
            return True


        rv = []
        def backtrack(k):
            if k == n:
                rv.append(list(map(lambda r : ''.join(r), board.copy())))
                return
            for i in range(n):
                if can_move(k,i):
                    board[k][i] = 'Q'
                    backtrack(k + 1)
                    board[k][i] = '.'



        backtrack(0)
        return rv

class Solution2:
    def solveNQueens(self,n):
        occupied_horizontals = set()
        occupied_verticals = set()
        occupied_diagonals = set()
        occupied_anti_diagonals = set()
        board = [['.'] * n for _ in range(n)]
        result = []

        def can_place(x,y):
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
                result.append(list(map(lambda x: ''.join(x), board[:])))
                return

            for i in range(n):
                if can_place(k,i):
                    place(k,i)
                    backtrack(k + 1)
                    remove(k,i)

        backtrack(0)
        return result

if __name__ == '__main__':
    boards = Solution2().solveNQueens(4)
    print(boards)

















