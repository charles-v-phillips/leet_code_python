from stuff import *
class Solution:
    def isSymmetric(self, root) -> bool:
        l = []
        def flatten(root):
            if root is None:
                return

            if root.right is None and root.left is not None:
                l.append(root.val)
                flatten(root.left)
                l.append(None)

            elif root.left is None and root.right is not None:
                l.append(None)
                flatten(root.right)
                l.append(root.val)

            else:
                flatten(root.left)
                l.append(root.val)
                flatten(root.right)

        flatten(root)
        print(l)
        while len(l) >1:
            left = l.pop(0)
            right = l.pop(len(l)-1)
            if left != right:
                return False
        return True

class Solution2:
    def isSymetric(self, root):

        def dfs(left, right):
            if left == None or right == None:
                return left == right
            if left.val != right.val:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)


        return root is None or dfs(root.left,root.right)




if __name__ == '__main__':
    s= Solution()
    t = createTree([1,2,2,None,3,3])
    print(s.isSymmetric(t))
