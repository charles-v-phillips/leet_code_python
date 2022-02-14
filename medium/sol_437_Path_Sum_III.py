from typing import Optional
from stuff.tree_stuff import TreeNode
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def helper(node,remaining):
            if not node:
                return 0

            if remaining == 0:
                print(f'{node.val=}')
                return 1 + helper(node, targetSum)

            return helper(node.right, remaining - node.val) + helper(node.left, remaining - node.val) +\
                   helper(node.left, targetSum - node.val) + helper(node.right, targetSum - node.val)

        return helper(root,targetSum)

from collections import defaultdict
class Solution2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        d = defaultdict(int)
        def dfs(node, remaining):
            nonlocal count
            if not node:
                return

            remaining += node.val

            if remaining == targetSum:
                count +=1

            count += d[remaining - targetSum]

            d[remaining] += 1
            dfs(node.left, remaining)
            dfs(node.right,remaining)
            d[remaining] -= 1
        dfs(root,0)
        return count











if __name__ == '__main__':
    print(Solution2().pathSum(root = TreeNode.list_to_tree([10,5,-3,3,2,None,11,3,-2,None,1]), targetSum = 8))






