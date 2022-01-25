class Solution(object):
    def allPathsSourceTarget(self, graph):
        paths = []
        partial_path = []
        visited = set()


        def dfs(node):

            partial_path.append(node)
            if node == len(graph) - 1:
                paths.append(partial_path.copy())
                partial_path.pop(len(partial_path)-1)
                return


            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

            partial_path.pop(len(partial_path) - 1)
            visited.remove(node)

        dfs(0)
        return paths

if __name__ == '__main__':
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    s = Solution()
    print(s.allPathsSourceTarget(graph))