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


class Solution2:
    def maxPathSum(self, root):
        best = float('-inf')
        def dfs(node):
            nonlocal best
            if not node:
                return 0
            path_left = max(dfs(node.left), 0)
            path_right = max(dfs(node.right), 0)

            best = max(best,node.val + path_left + path_right)
            return node.val + max(path_left,path_right)
        dfs(root)

        return best






if __name__ == '__main__':
    print(Solution2().maxPathSum(TreeNode.list_to_tree([-1,-2,-3])))