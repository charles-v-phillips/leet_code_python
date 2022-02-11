class Solution:
    def coinChange(self, coins, amount) -> int:
        coins = sorted(coins, reverse=True)
        min_depth = float('inf')
        def dfs(amount,depth):
            nonlocal min_depth
            if amount == 0:
                min_depth = min(min_depth,depth)
                return
            if amount < 0:
                return
            if depth >= min_depth:
                return

            for coin in coins:
                dfs(amount - coin,depth + 1)

        dfs(amount,0)
        return min_depth if min_depth != float('inf') else -1

class Solution2:
    def coinChange(self, coins, amount) -> int:
        min_depth = float('inf')
        memo = {}
        def dfs(amount, depth):
            nonlocal min_depth
            if amount == 0:
                min_depth = min(min_depth, depth)
                return min_depth

            if amount < 0 or min_depth < depth:
                return float('inf')

            if (amount, depth) in memo:
                return memo[(amount,depth)]


            m_d = min(dfs(amount - coin, depth + 1) for coin in coins)

            memo[(amount,depth)] = m_d
            return m_d

        dfs(amount,0)
        return min_depth if min_depth != float('inf') else -1


class Solution3:
    def coinChange(self, coins, amount) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1,len(dp)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],1 + dp[i - coin])

        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    print(Solution3().coinChange([1, 2, 5], 11))

