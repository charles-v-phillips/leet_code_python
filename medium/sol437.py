from stuff import *
class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        l = []
        self.num = 0
        def helper(node : TreeNode):
            if not node: return

            l.insert(0,node.val)
            helper(node.left)
            helper(node.right)
            sum = 0
            for e in l:
                sum+=e
                if sum == targetSum:
                    self.num+=1
            l.pop(0)
        helper(root)
        return self.num

if __name__ == '__main__':
    t = createTree([10,5,-3,3,2,None,11,3,-2,None,1])
    s = Solution()
    print(s.pathSum(t,8))

