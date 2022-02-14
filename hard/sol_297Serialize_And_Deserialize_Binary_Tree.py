from collections import deque
from stuff.tree_stuff import TreeNode
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if not node:
                result.append('*,')
                continue
            result.append(str(node.val) + ',')


            q.append(node.left)
            q.append(node.right)

        return ''.join(result)




    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')



        root = TreeNode(data[0])
        q = deque()
        q.append(root)
        i = 1
        while i < len(data) - 1:
            node = q.popleft()

            if data[i] == '*':
                node.left = None
            else:
                node.left = TreeNode(int(data[i]))
                q.append(node.left)


            i += 1
            if i >= len(data) - 1:
                continue


            if data[i] == '*':
                node.right = None
            else:
                node.right = TreeNode(int(data[i]))
                q.append(node.right)

            i += 1

        return root








if __name__ == '__main__':
    codec = Codec()

    print(codec.serialize(root = TreeNode.list_to_tree([])))
