from stuff.tree_stuff import TreeNode
class Solution:

    def closestValue(root, target):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        l = inorder(root)
        return min(l,key= lambda x: abs(target - x))





if __name__ == '__main__':
    print(Solution.closestValue(root = TreeNode.list_to_tree([4,2,5,1,3]), target = 3.714286))