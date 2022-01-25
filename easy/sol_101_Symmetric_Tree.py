from stuff.tree_stuff import TreeNode
class Solution:
    def isSymmetric( root):
        def helper(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            b1 = n1.val == n2.val
            b2 = helper(n1.left, n2.right)
            b3 = helper(n1.right, n2.left)
            return b1 and b2 and b3

        return helper(root.left, root.right)

if __name__ == '__main__':
    print(Solution.isSymmetric(TreeNode.list_to_tree([1,2,2,3,4,4,3])))