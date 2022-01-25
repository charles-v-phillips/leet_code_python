from stuff import *

class Solution:
    def rob(self, root) -> int:
        def dfs(node,depth):
            if node == None:
                return 0
            if depth % 2 == 0:
                return node.val + dfs(node.left,depth+1) + dfs(node.right,depth+1)
            else:
                return dfs(node.left,depth+1) + dfs(node.right,depth+1)


        return max(dfs(root,0),dfs(root.left,0) + dfs(root.right,0))


class Solution2:
    def rob(self, root)-> int:
        def rob_from_root(node):
            if node is None:
                return 0

            return node.val + rob_from_children(node.left) + rob_from_children(node.right)

        def rob_from_children(node):
            if node is None:
                return 0

            return self.rob(node.left) + self.rob(node.right)



        if root is None: return 0
        return max(rob_from_root(root),rob_from_children(root))

if __name__ == '__main__':
    s = Solution2()
    t = createTree([3,2,3,None,3,None,1])
    print(s.rob(t))
