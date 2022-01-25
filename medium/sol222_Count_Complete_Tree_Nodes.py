from stuff import *
class Solution:
    def countNodes(self, root) -> int:
        def get_depth(node):
            if not node: return 0
            return 1 + get_depth(node.left)

        self.depth = get_depth(root)
        self.guaranteed_min_num_nodes = sum([2**k for k in range(self.depth - 1)])
        self.num_in_last_row = 0

        def probe(node,d):
            if not node and d == self.depth:
                return True #true means weve found the boundary, wve found the last node in the last level and can return

            if node and d == self.depth:
                self.num_in_last_row +=1
                return False

            if probe(node.left,d+1):
                return True
            if probe(node.right,d+1):
                return True


        if not root: return 0
        probe(root,1)
        return self.guaranteed_min_num_nodes + self.num_in_last_row

class Solution2:
    def get_depth(self,node):
        if not node:
            return 0
        return 1 + self.get_depth(node.left)

    def countNodes(self,root):
        if not root:
            return 0

        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth == right_depth:
            return pow(2,left_depth) + self.countNodes(root.right)
        else:
            return pow(2,right_depth) + self.countNodes(root.left)














if __name__ == '__main__':
    print(Solution().countNodes(createTree([1,2,3,4,5,6])))

