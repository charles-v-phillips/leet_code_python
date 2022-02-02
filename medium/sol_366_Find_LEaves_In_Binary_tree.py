from typing import Optional, List
from stuff.tree_stuff import TreeNode
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, l):
            if not node.left and not node.right:
                l.append(node.val)
                return None
            if node.right:
                node.right = helper(node.right,l)
            if node.left:
                node.left = helper(node.left, l)

            return node



        rv = []
        while root:
            print(rv)
            l = []
            root = helper(root,l)
            rv.append(l)

        return rv

if __name__ == '__main__':
    print(Solution().findLeaves(TreeNode.list_to_tree([1,2,3,4,5])))
