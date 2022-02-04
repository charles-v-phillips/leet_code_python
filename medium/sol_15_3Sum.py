import collections


class Solution:
    def twoSum(self, nums, i):
        r = len(nums) - 1
        l = i + 1
        rv = []
        while l < r:
            tot = nums[l] + nums[r] + nums[i]
            if  tot == 0:
                rv.append([nums[l],nums[r],nums[i]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1


            elif tot < 0:
                l += 1
            else:
                r -=1
        return rv









    def threeSum(self, nums):
        nums = sorted(nums)
        rv = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                rv.extend(self.twoSum(nums, i))
        return rv

if __name__ == '__main__':
    print(Solution().threeSum(nums = [0,0,0,0]))






