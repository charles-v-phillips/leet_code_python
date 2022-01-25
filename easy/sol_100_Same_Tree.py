from stuff.tree_stuff import TreeNode
class Solution:
    def isSameTree(self, p, q):
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            return node1.val == node2.val and dfs(node1.left,node2.left) and dfs(node1.right, node2.right)
        return dfs(p,q)

if __name__ == '__main__':
    print(Solution().isSameTree(TreeNode.list_to_tree([1,2]), TreeNode.list_to_tree([1,None,2])))