from stuff.tree_stuff import TreeNode
from typing import Optional

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.l = []
        self.index = 0
        def construct_list(node):
            if node == None:
                return
            construct_list(node.left)
            self.l.append(node.val)
            construct_list(node.right)
        construct_list(root)


    def next(self) -> int:
        if self.hasNext():
            val = self.l[self.index]
            self.index += 1
            return val


    def hasNext(self) -> bool:
        return self.index < len(self.l)

class BSTIterator2:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        if not self.hasNext():
            return

        node = self.stack.pop()
        val = node.val
        if not node.right:
            return val

        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return val



    def hasNext(self) -> bool:
        return bool(self.stack)





if __name__ == '__main__':
    it = BSTIterator2(TreeNode.list_to_tree([7, 3, 15, None, None, 9, 20]))
    print('hi')
    print(it.next())
    print(it.next())
    print(it.next())
    print(it.next())
    print(it.next())
    print(it.next())

