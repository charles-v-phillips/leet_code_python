class Solution:
    def coinChange(self, coins, amount) -> int:
        coins = sorted(coins, reverse=True)
        min_depth = float('inf')
        def dfs(amount,depth):
            print(depth, end = '\r')
            nonlocal min_depth
            if amount == 0:
                print(depth, min_depth)
                min_depth = min(min_depth,depth)

                return
            if amount < 0:
                return

            for coin in coins:
                dfs(amount - coin,depth + 1)


        dfs(amount,0)
        return min_depth if min_depth != float('inf') else -1




        dfs(amount,0)
        return min_depth if min_depth != float('inf') else -1

if __name__ == '__main__':
    # print(Solution().coinChange([186,419,83,408], 6249))
    d = {a:b for a, b in zip(range(3),range(3)) }
    print([k for k in d if d[k] > 1])