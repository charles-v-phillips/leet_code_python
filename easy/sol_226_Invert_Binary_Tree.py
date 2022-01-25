from stuff.tree_stuff import TreeNode
class Solution:
    def invertTree(self, root):
        def helper(node):
            if not node:
                return None
            node.left ,node.right = node.right, node.left
            node.left = helper(node.left)
            node.right = helper(node.right)
            return node
        helper(root)
        return root
if __name__ == '__main__':
    Solution().invertTree(TreeNode.list_to_tree([4,2,7,1,3,6,9]))
