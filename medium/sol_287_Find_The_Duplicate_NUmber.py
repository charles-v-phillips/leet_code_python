from typing import List
## Negative Marking
class Solution:
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        for i, e in enumerate(nums):
            if nums[abs(e)] < 0:
                return abs(e)
            nums[abs(e)] = min(nums[abs(e)],-nums[abs(e)])




if __name__ == '__main__':
    print(Solution.findDuplicate(nums = [1,2,2]))
    print(Solution.findDuplicate(nums=[1,3,4, 2, 2]))