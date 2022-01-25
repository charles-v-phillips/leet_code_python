from stuff import Node



class Solution(object):

    def cloneGraph(self, node):


        def dfs(node):
            if node.val in createdNodes.keys():
                return createdNodes[node.val]

            c = Node(node.val)
            createdNodes[c.val] = c

            for n in node.neighbors:
                c.neighbors.append(dfs(n))
            return c

        createdNodes = {}
        return dfs(node)



if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.neighbors = [n3,n5]
    n2.neighbors = [n3,n4,n5]
    n3.neighbors = [n2,n1]
    n4.neighbors = [n2]
    n5.neighbors = [n1,n2]

    s = Solution()
    clone = s.cloneGraph(n1)
    print("HERE")



