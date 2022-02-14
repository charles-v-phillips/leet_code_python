from stuff.tree_stuff import TreeNode
from typing import Optional
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right, targetSum)



if __name__ == '__main__':
    # print(Solution().hasPathSum(TreeNode.list_to_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]), targetSum = 22))
    print(Solution().hasPathSum(TreeNode.list_to_tree([1, 2]),
                                targetSum=1))

