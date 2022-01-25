from typing import List
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda x: nums[x] - (nums[0] + x)

        n = len(nums)
        if k > missing(n-1):
            return nums[-1] + (k - missing(n-1))

        l, r = 0, n-1
        while l != r:
            mid = (l+r)//2
            if missing(mid) < k:
                l = mid + 1
            else:
                r = mid


        return nums[l-1] + (k - missing(l-1))




if __name__ == '__main__':
    print(Solution().missingElement([4,7,9,10],0))