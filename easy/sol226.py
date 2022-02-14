from stuff.tree_stuff import TreeNode

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


class Solution2:

    def helper(self, node):
        if not node:
            return None
        node.left, node.right = self.helper(node.right), self.helper(node.left)
        return node


    def invertTree(self, root):
        return self.helper(root)


if __name__ == '__main__':
    inverted = Solution2().invertTree(root = TreeNode.list_to_tree([4,2,7,1,3,6,9]))
    print('hi')