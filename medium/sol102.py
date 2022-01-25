class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        q.append(root)
        rv = []

        while len(q) != 0:
            l = len(q);
            level = []
            for i in range(l):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level.append(node.val)

            rv.append(level)

            
        return rv

