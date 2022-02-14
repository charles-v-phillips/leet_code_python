from typing import Optional
from stuff.tree_stuff import TreeNode
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(node):
            nonlocal longest
            if not node.left and not node.right:
                return 1


            path_left = dfs(node.left)
            path_right = dfs(node.right)

            if node.left.val == node.val == node.right.val:
                longest = max(longest, 1 + path_left + path_right)


            if node.val == node.left.val:
                path_left +=1

            elif node.val == node.right.val:
                path_right += 1
            else:
                return 0

            return max(path_left,path_right)
        dfs(root)
        return longest - 1

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent_value):
            if not node:
                return 1

            path_left = dfs(node.left,node.val)
            path_right = dfs(node.right,node.val)

            if node.val == parent_value:
                pass



        longest = 0
        dfs(root,-1)
        return longest - 1



if __name__ == '__main__':
    Solution().longestUnivaluePath(TreeNode.list_to_tree( [1,4,5,4,4,5]))









