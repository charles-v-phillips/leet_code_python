import math
class Solution:
    def minEatingSpeed(self, piles, h):
        def can_finish(rate):
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile/rate)
            return num_hours <= h
        # r = 1
        # while True:
        #     if can_finish(r):
        #         return r
        #     r += 1

        l, r = 0, max(piles)

        while l <= r:
            mid = (l + r)//2
            if can_finish(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l














if __name__ == '__main__':
    # print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5)) #30
    # print(Solution().minEatingSpeed(piles = [3, 6, 7, 11], h = 8))  # 4
    # print(Solution().minEatingSpeed(piles=[312884470], h=312884469 ))
    print(Solution().minEatingSpeed([312884470], 968709470))


