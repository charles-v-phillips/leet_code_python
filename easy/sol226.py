from stuff import TreeNode

class Solution:
    def helper(self,root):
        if root == None:
            return None
        dummy = root.right
        root.right = root.left
        root.left = dummy
        root.left = self.helper(root.left)
        root.right = self.helper(root.right)

        return root


    def invertTree(self, root):
        return self.helper(root)


if __name__ == '__main__':
    None
