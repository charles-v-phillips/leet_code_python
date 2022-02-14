from typing import Optional, List
from stuff.tree_stuff import TreeNode
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        def dfs(node, i):
            if not node:
                return
            dfs(node.left, i - 1)
            d[i].append(node.val)
            dfs(node.right, i + 1)

        dfs(root,0)
        result = [d[key] for key in d]
        return result

from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        q = deque()
        q.append((root, 0))

        while q:
            node, col = q.popleft()
            if node:
                d[col].append(node.val)
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))

        return [d[key] for key in sorted(d.keys())]




if __name__ == '__main__':
    print(Solution().verticalOrder(TreeNode.list_to_tree([3,9,8,4,0,1,7])))



