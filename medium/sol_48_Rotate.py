import math


class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



        for i in range(n):
            l = 0
            r = n-1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -=1

        for i in range(n):
            print(matrix[i])


class Solution2:
    def rotate_outer(self,matrix, i, n):
        for j in range(i,n):

            temp = matrix[i][j]
            matrix[i][j] = matrix[i + n-j][i]
            matrix[ i + n - j][i] = matrix[n][i + n - j]
            matrix[n][i  + n - j] = matrix[j][n]
            matrix[j][n] = temp




    def rotate(self, matrix) -> None:
        i = 0
        n = len(matrix) - 1
        while i <= n:
            self.rotate_outer(matrix, i, n)
            i += 1
            n -= 1
        return matrix



if __name__ == '__main__':
    #
    # rotated = Solution2().rotate(matrix = [[1, 2],[3, 4]])
    # for e in rotated:
    #     print(e)
    #
    # rotated = Solution2().rotate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # for e in rotated:
    #     print(e)

    rotated = Solution2().rotate(matrix = [list(range(i, i + 6)) for i in range(1,37,6)])
    for e in rotated:
        print(e)

    # rotated = Solution2().rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
    # for e in rotated:
    #     print(e)






