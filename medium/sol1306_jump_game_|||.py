class Solution:
    def canReach(self, arr, start) -> bool:
        visited = [False]*len(arr)
        def dfs(arr, pos):
            if arr[pos] == 0:
                return True
            visited[pos] = True

            if pos - arr[pos] >=0 and not visited[pos - arr[pos]] and dfs(arr,pos - arr[pos]):
                return True
            if pos + arr[pos] <len(arr) and not visited[pos + arr[pos]] and dfs(arr,pos + arr[pos]):
                return True
            visited[pos] = False
            return False

        def dfs2(arr,pos):
            if pos <0 or pos >= len(arr) or visited[pos]:
                return False

            if arr[pos] == 0:
                return True

            visited[pos] = True

            return dfs2(arr,pos - arr[pos]) or dfs2(arr,pos + arr[pos])





        return dfs(arr,start)
if __name__ == '__main__':
    s = Solution()
    print(s.canReach([3,0,2,1,2],2))








