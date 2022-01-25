from stuff.tree_stuff import TreeNode
class Solution:
    def upsideDownBinaryTree( root):
        def helper(node):
            if not node:
                return None
            node.left = helper()
if __name__ == '__main__':
    Solution.upsideDownBinaryTree(TreeNode.list_to_tree([1,2,3,4,5]))