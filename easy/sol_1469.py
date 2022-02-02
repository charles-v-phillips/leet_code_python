from stuff.tree_stuff import TreeNode
from typing import Optional, List
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return []
        if root.left and not root.right:
            return self.getLonelyNodes(root.left) + [root.left.val]
        if not root.left and root.right:
            return self.getLonelyNodes(root.right) + [root.right.val]

        return self.getLonelyNodes(root.left) + self.getLonelyNodes(root.right)

if __name__ == '__main__':
    print(Solution().getLonelyNodes(TreeNode.list_to_tree( [1,2,3,None,4])))