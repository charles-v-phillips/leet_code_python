from stuff import *
class Solution:
    def generateTrees(self, n: int):
        rv = []

        def generate_tree(l, u):
            if l >= u:
                return None

            for i in range(l, u+1):
                node = TreeNode(i)
                node.left = generate_tree(l, i-1)
                node.right = generate_tree(i+1, u)
                


                return node




        generate_tree(1, n)

        return rv

if __name__ == '__main__':
    s = Solution()
    s.generateTrees(3)
