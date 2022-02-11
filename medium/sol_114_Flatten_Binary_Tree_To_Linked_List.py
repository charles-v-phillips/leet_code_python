from stuff.tree_stuff import TreeNode
from typing import Optional
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def get_most_right(node):
            while node.right:
                node = node.right
            return node
        def helper(node):
            if not node:
                return
            helper(node.left)
            if node.left:
                get_most_right(node.left).right = node.right
                node.right = node.left
                node.left = None
            helper(node.right)
        helper(root)
        print('hi')



if __name__ == '__main__':
    Solution().flatten(TreeNode.list_to_tree( [1,2,5,3,4,None,6]))





