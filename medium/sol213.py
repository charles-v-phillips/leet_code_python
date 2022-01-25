class Solution:
    def rob(self, nums) -> int:
        if len(nums) <=2:
            return max(nums)

        started_1 = [0 for _ in range(len(nums)+1)]
        started_2 = [0 for _ in range(len(nums) + 1)]

        #padding
        started_1[0] = 0
        started_1[1] = nums[0]
        started_2[0] = 0
        started_2[1] = 0

        for i in range(2,len(nums)+1):
            started_1[i] = max(started_1[i-1],started_1[i-2] + nums[i-1])
            started_2[i] = max(started_2[i-1],started_2[i-2] + nums[i-1])

        return max(started_1[i-1],started_2[i])

if __name__ == '__main__':
    s = Solution()
    print(s.rob([200,3,140,20,10]))


