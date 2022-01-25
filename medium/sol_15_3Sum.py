class Solution:
    def threeSum(self, nums):
        rv = []
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if nums[i]+nums[j]+nums[k]==0:
                        rv.append([nums[i],nums[j],nums[k]])

        return rv

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
