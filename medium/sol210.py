class Solution:
    def findOrder(self, numCourses, prerequisites):
        # visited = [False for _ in range(numCourses)]
        # path = []
        in_degree = [0 for _ in range(numCourses)]
        g = {}

        for i in range(numCourses):
            g[i] = []
        for p in prerequisites:
            g[p[1]].append(p[0])
            in_degree[p[0]]+=1


        zero_degree = [i for i in range(numCourses) if in_degree[i] == 0 ]

        path = []
        while len(zero_degree) != 0:
            node1 = zero_degree.pop(0)
            path.append(node1)
            for node2 in g:
                if node2 in g[node1]:
                    g[node1].remove(node2)
                    in_degree[node2]-=1
                    if in_degree[node2]==0:
                        zero_degree.append(node2)

        for node in g:
            if len(g[node]) != 0:
                return []
        return path



class Solution2:
    def findOrder(self,numCourses, prerequisites):
        visited = [False for _ in range(numCourses)]
        g = {}
        path = []
        processed = [False for _ in range(numCourses)]
        for i in range(numCourses):
            g[i] = []
        for p in prerequisites:
            g[p[1]].append(p[0])

        def dfs(i): #RETURNS TRUE IF CYCLE IS DETECTED
            if visited[i] and not processed[i]:
                print("Cycle Detected")
                return True
            if processed[i]:
                return False
            visited[i] = True
            for neigh in g[i]:
                if dfs(neigh): return True

            path.insert(0, i)
            processed[i] = True



        for c in range(numCourses):
            if not visited[c]:
                if dfs(c):
                    return []


        return path












if __name__ == '__main__':
    s = Solution2()
    # print(s.findOrder(2,[[0,1],[1,0]]))
    print(s.findOrder(2,[[1,0]]))
    # print(s.findOrder(4,[[1, 0], [2, 0], [3, 1], [3, 2]]))
