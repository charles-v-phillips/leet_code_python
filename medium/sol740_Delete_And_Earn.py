import collections
class Solution:
    def deleteAndEarn(self, nums) -> int:
        def pick(num,dummy):
            dummy.remove(num)
            rv = [x for x in dummy if x-1 != num and x+1 != num]


            return num,rv

        def do(arr):
            if len(arr) == 0:
                return 0
            mv = 0

            for i in range(len(arr)):
                d = arr.copy()
                p,resultant_array = pick(d[i],d)
                val = p + do(resultant_array)
                if val > mv:
                    mv = val
            return mv
        return do(nums)

class Solution2:
    def deleteAndEarn(self,nums):
        count = collections.Counter(nums)

        gold = [0 if k not in count.keys() else k*count[k] for k in range(max(nums)+1)]

        dp = [0 for _ in range(len(gold)+1)]
        dp[1] = gold[0]
        for i in range(1,len(gold)):
            dp[i+1] = max(dp[i-1] + gold[i],dp[i])
        return dp[-1]





if __name__ == '__main__':
    print(Solution2().deleteAndEarn([3,4,2,]))











