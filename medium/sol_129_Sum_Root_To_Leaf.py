from typing import Optional
from stuff.tree_stuff import TreeNode
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node.left:
                return [str(node.val)]
            if not node.right:
                return [str(node.val)]

            str_val = str(node.val) if node.val != 0 else ''
            num_left = [str_val + num for num in helper(node.left)]

            num_right = [str_val + num for num in helper(node.right)]

            return num_left + num_right

        return sum( int(num) for num in helper(root))


class Solution2:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(node, cur_val):
            nonlocal tot_val
            if node:
                cur_val = 10 * cur_val + node.val
                if not (node.left or node.right):
                    tot_val += cur_val


                helper(node.left, cur_val)
                helper(node.right, cur_val)

        tot_val = 0
        helper(root, 0)
        return tot_val









if __name__ == '__main__':
    # print(Solution2().sumNumbers(TreeNode.list_to_tree([0,1])))
    print(Solution2().sumNumbers(TreeNode.list_to_tree( [1,2,3])))
    # print(Solution().sumNumbers(TreeNode.list_to_tree([4,9,0,5,1])))

