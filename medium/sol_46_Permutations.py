class Solution:

    def permute(self, nums):
        rv = []
        partial_list = []
        def swap(l,i,j):
            l[i],l[j] = l[j],l[i]

        def bt(i):
            if i == len(nums):
                if nums in rv:
                    return
                rv.append(nums.copy())
                return

            for k in range(i,len(nums)):
                bt(k+1)
                swap(nums,k,i)
                bt(k+1)

        bt(0)
        return rv

class Solution2:
    def permute(self, nums):
        visited = [False]*len(nums)
        path = []
        rv = []
        def dfs():
            if len(path) == len(nums):
                rv.append(path.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs()
                path.remove(nums[i])
                visited[i] = False


        dfs()
        return rv









if __name__ == '__main__':
    l = [1,2,3,4]
    print(Solution2().permute(l))


