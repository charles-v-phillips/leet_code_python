class Solution:
    def maxProfit(self, prices):
        def helper(i):
            vals = [prices[k] - prices[i] for k in range(i+1,len(prices))]
            return max(vals) if len(vals) >0 else 0
        max_val = 0
        for i in range(len(prices)):
            max_val = max(max_val,helper(i))
        return max_val




if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))

