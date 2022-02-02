class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, e in enumerate(nums):
            if target - e in d:
                return [d[target - e], i]
            d[e] = i
        return []

    def threeSum(self, nums):
        max()








if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
