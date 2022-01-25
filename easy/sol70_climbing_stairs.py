class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i):
            if i == n:
                return 1
            if i>n:
                return 0

            return helper(i+1) + helper(i+2)

        return helper(0)

class Solution2:
    def climbStairs(self,n : int)-> int:
        if n <=2:
            return n
        s_0 = 1
        s_1 = 2
        for i in range(2,n):
            s_next = s_0 + s_1
            s_0 = s_1
            s_1 = s_next

        return s_next
if __name__ == '__main__':
    s = Solution2()
    print(s.climbStairs(2))
