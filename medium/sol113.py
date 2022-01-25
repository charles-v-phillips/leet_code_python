from stuff import *
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        if not root: return []
        paths = []
        path = []

        def search(root:TreeNode, targetSum: int):
            if not root.left and not root.right and targetSum - root.val == 0:
                path.append(root.val)
                paths.append(path.copy())
                return

            if not root.left and not root.right :
                path.append(root.val)
                return

            path.append(root.val)
            newTarget  = targetSum - root.val

            if root.left:
                search(root.left,newTarget)
                path.pop()

            if root.right:
                search(root.right,newTarget)
                path.pop()



        search(root,targetSum)
        return paths

if __name__ == '__main__':
    s = Solution()
    l = s.pathSum(createTree([5,4,8,11,None,13,4,7,2,None,None,5,1]),22)
    print(l)

