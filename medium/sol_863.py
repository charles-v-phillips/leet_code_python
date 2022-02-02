from typing import List
from stuff.tree_stuff import TreeNode
class Solution:
    ## OOPS DIDNT READ QUESTION
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        if k == 0:
            return [root.val]

        return self.distanceK(root.right,1, k-1) + self.distanceK(root.left,1, k - 1)


class Solution2:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def distance_to(source, target):
            if not source:
                return float('-inf')
            if source.val == target:
                return 0

            return 1 + max(distance_to(source.left, target),distance_to(source.right, target))
        return distance_to(root, target)








if __name__ == '__main__':
    print(Solution2().distanceK(TreeNode.list_to_tree([3,5,1,6,2,0,8,None,None,7,4]),12, 2))