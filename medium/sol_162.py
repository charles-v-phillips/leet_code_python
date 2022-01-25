from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def helper(l,r):
            if l == r:
                return l
            mid = (l + r)//2
            mid2 = mid + 1
            if nums[mid] < nums[mid2]:
                return helper(mid2,r)
            else:
                return helper(l, mid)
        return helper(0, len(nums)-1)

if __name__ == '__main__':
    print(Solution().findPeakElement(nums = [2,1]))


