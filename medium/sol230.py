from stuff import TreeNode

l = []
class Solution(object):
    def flatten(self,root):
        if root == None:
            return
        self.flatten(root.left)
        l.append(root.val)
        self.flatten(root.right)
    def kthSmallest(self, root, k):
        self.flatten(root)
        return l[k-1]


if __name__ == '__main__':
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(5)
    t.left.right = TreeNode(3)
    s = Solution()
    print(s.kthSmallest(t,1))
    print(l)

