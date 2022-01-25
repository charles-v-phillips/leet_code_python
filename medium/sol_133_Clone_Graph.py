class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def cloneGraph(self, node):
        if not node:
            return None
        seen = {}
        def helper(node):
            if node.val in seen:
                return seen[node.val]
            copy = Node(val=node.val)
            seen[copy.val] = copy

            for n in node.neighbors:
                copy.neighbors.append(helper(n))
            return copy
        return helper(node)


if __name__ == '__main__':
    pass
