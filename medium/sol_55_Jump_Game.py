class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums) - 1

        def dfs(pos):
            if pos == n:
                return True
            if pos > n:
                return False

            for step in range(1,nums[pos]+1):
                if dfs(pos + step):
                    return True

            return False

        return dfs(0)


class Solution2:
    def canJump(self, nums):
        mx = 0
        for i, num in enumerate(nums):
            if i > mx:
                return False
            mx = max(mx,i + num)



if __name__ == '__main__':
    Solution2().canJump(nums = [2,3,1,1,4])