class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    def twoSum(self, nums, target):
        d = {}
        for i,e in enumerate(nums):
            d[e] = i
        for i in range(len(nums)):
            if target - nums[i] in d.keys() and d[target - nums[i]] != i:
                return [d[target-nums[i]],i]



if __name__ == '__main__':
    print(Solution2().twoSum(nums=[2, 7, 11, 15], target=9))
