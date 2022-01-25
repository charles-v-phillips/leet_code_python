from stuff import TreeNode

class BSTIterator:

    def __init__(self, root):
        self.root = root
        self.l = self._flatten(root)

    def _flatten(self,root):
        if root == None:
            return []
        return self._flatten(root.left) + [root.val] + self._flatten(root.right)

    def next(self) -> int:
        return self.l.pop(0)

    def hasNext(self) -> bool:
        return len(self.l) != 0

if __name__ == '__main__':
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(5)
    t.left.right = TreeNode(3)

    it = BSTIterator(t)
    print(it.l)