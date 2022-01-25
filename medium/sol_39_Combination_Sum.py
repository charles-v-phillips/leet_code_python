class Solution:
    def combinationSum(self, candidates, target: int):
        rv = []
        def dfs(tot,p,candidates):
            if tot == target:
                rv.append(p)
                return
            if tot > target:
                return

            for i,c in enumerate(candidates):
                dfs(tot+c,p + [c],candidates[i:])
        dfs(0,[],candidates)
        return rv



if __name__ == '__main__':


    print(Solution().combinationSum([2,3,6,7],7))

    i = 2
    l = [1,2,3,4,5]
    for i in range(len(l)):
        print(i)
    print(f'{i=}')
