class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def createTree(l):
    q = []
    root = TreeNode(l[0])
    i = 1
    q.append(root)

    while i < len(l):
        n = q.pop(0)
        if l[i] != None:
            n.left = TreeNode(l[i])
            q.append(n.left)
            i+=1
        else:
            i+=1

        if i < len(l) and l[i] != None:
            n.right = TreeNode(l[i])
            q.append(n.right)
            i+=1
        else:
            i+=1
    return root









if __name__ == '__main__':
    t = createTree([1,2,2,2,None,2])
    print("HEre")







