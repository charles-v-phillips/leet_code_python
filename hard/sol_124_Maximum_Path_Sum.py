from stuff.tree_stuff import TreeNode
class Solution:
    def maxPathSum(self, root) -> int:
        def helper(node):
            if not node:
                return 0
            l = node.val + helper(node.left)
            r = node.val + helper(node.right)
            return max(l,r)



        return helper(root)


if __name__ == '__main__':
    print(Solution().maxPathSum(TreeNode.list_to_tree([-10,9,20,None,None,15,7])))