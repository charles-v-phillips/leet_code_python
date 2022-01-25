class Solution:

    #Naive recursive solution, should be correct, just hits TLE sometimes
    def jump(self, nums) -> int:
        min_steps = [-1]*len(nums)
        def helper(nums,index):
            if index >= len(nums) - 1:return 0
            if min_steps[index] != -1:
                return min_steps[index]
            l = [1 + helper(nums,index + i) for i in range(1,nums[index]+1)]
            if len(l) == 0 and index + 1 == len(nums)-1:
                return 1
            if len(l) == 0 and index + 1 != len(nums)-1:
                return float('inf')
            mini = min(l)
            min_steps[index] = mini
            return mini

        return helper(nums,0)

class Solution2:
    def jump(self,nums) -> int:
        l,r = 0, nums[0]
        jumps = 1
        while r < len(nums) - 1:
            jumps +=1
            next = max([i + nums[i] for i in range(l,r+1)])
            l = r+1
            r = next
        return jumps










if __name__ == '__main__':
    s=  Solution2()
    print(s.jump([2,3,1,1,4])) #2
    print(s.jump([2, 3, 0, 1, 4])) #2
    print(s.jump([1,2])) #1
    print(s.jump([2,0,2,4,6,0,0,3])) #3
    print(s.jump([2,1,1,1,1]))#3


