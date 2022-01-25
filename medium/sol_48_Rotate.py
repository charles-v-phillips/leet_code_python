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




        # for i in range(n):
        #     l = 0
        #     r = n-1
        #     while l < r:
        #         matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]








if __name__ == '__main__':
    Solution().rotate(matrix = [[5,1,9,11],
                                [2,4,8,10],
                                [13,3,6,7],
                                [15,14,12,16]])
