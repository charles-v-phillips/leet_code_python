# class TreeNode(object):
#      def __init__(self, val=0, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

from stuff import TreeNode


class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))



if __name__ == '__main__':
    t = TreeNode(5)
    s = Solution()
    print(s.maxDepth(t))
