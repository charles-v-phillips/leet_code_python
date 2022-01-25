class Solution:
    def searchMatrix(self, matrix, target: int):
        def map2(i):
            return divmod(i,len(matrix[0]))

        l = 0
        r = len(matrix)*len(matrix[0])
        while l < r:
            mid = int((l+r)/2)
            x,y = map2(mid)
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                r = mid
            if matrix[x][y] < target:
                l = mid + 1
        return False



if __name__ == '__main__':
    print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))




