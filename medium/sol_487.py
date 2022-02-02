from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = r = 0
        max_len =0

        num_zeros_seen = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0 and num_zeros_seen < 1:
                r += 1
                num_zeros_seen +=1
            else:
                r +=1
                l = r
                num_zeros_seen = 0
            max_len = max(max_len, r - l)

        return max_len

class Solution2:
    def findMaxConsecutiveOnes(selfself,nums):
        l = r = max_len = num_zeros_seen = last_seen_zero = 0

        while r < len(nums):
            if nums[r] == 0 and num_zeros_seen == 0:
                num_zeros_seen = 1
                last_seen_zero = r


            elif nums[r] == 0 and num_zeros_seen != 0:
                l = last_seen_zero + 1
                last_seen_zero = r
            else:
                pass
            r += 1
            max_len = max(max_len, r - l)
        return max_len












if __name__ == '__main__':
    print(Solution2().findMaxConsecutiveOnes([1,0,1,1,0]))
    print(Solution2().findMaxConsecutiveOnes([0]))
