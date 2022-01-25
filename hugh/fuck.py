from collections import deque
class Solution:
    def robber(self,nums):
        m0 = nums[0]
        m1 = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            temp = m1
            m1 = max(m0 + nums[i],m1)
            m0 = temp

        return m1

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        l = deque()

        while x:
            x,last = divmod(x, 10)
            l.append(last)
            # x = int((x - last) / 10)
        print(l)

        while len(l) > 1:
            if l.popleft() != l.pop():
                return False
        return True
        # x_str = str(x)
        # h_ind = len(x_str)
        # mid = h_ind // 2
        # if len(x_str) % 2 != 0:
        #     beg = x_str[:(mid)]
        #     end = x_str[(mid + 1):]
        #     return beg == end[::-1]
        # else:
        #     beg = x_str[:mid]
        #     end = x_str[mid:]
        #     return beg == end[::-1]

if __name__ == '__main__':
    print(Solution().isPalindrome(33433))





