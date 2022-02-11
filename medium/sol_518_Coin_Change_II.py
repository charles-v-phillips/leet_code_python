from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = 0
        def dfs(amount,purse):
            nonlocal count
            if amount == 0:
                count +=1
                print(purse)
                return
            if amount < 0:
                return

            for coin in coins:
                dfs(amount - coin,purse + [coin])

        dfs(amount,[])
        return count

class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]


if __name__ == '__main__':
    print(Solution2().change(5, coins = [1, 2, 5]))


