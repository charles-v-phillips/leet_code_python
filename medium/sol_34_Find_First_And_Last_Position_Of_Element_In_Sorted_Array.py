class Solution:
    def searchRange(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            mid = int((l+r)/2)
            if mid == target:
                if mid > 0 and target[mid-1]:
                    pass



        pass
if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10],8))
