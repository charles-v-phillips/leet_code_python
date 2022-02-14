from typing import Optional,List
from stuff.tree_stuff import TreeNode
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        rv = []
        def dfs(node, partial, target_Sum):
            if not node:
                return

            partial.append(node.val)

            if not node.left and not node.right and target_Sum == node.val:
                rv.append(partial[:])

            dfs(node.left, partial, target_Sum - node.val)
            dfs(node.right, partial, target_Sum - node.val)
            partial.pop()

        dfs(root, [], targetSum)
        return rv




if __name__ == '__main__':
    print(Solution().pathSum(TreeNode.list_to_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), targetSum = 22))






