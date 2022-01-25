from collections import deque
class TreeNode:
    def __init__(self,val = None,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right


    def list_to_tree(l):

        root = TreeNode(l[0])
        q = deque()
        idx = 1
        q.append(root)

        while idx < len(l) and q:
            num = len(q)
            for i in range(num):
                node = q.popleft()
                if idx < len(l) and  l[idx] != None:
                    node.left = TreeNode(l[idx])
                    q.append(node.left)
                    idx += 1
                else:
                    idx += 1

                if idx < len(l) and l[idx] != None:
                    node.right = TreeNode(l[idx])
                    q.append(node.right)
                    idx +=1
                else:
                    idx +=1
        return root







if __name__ == '__main__':
    print(TreeNode.list_to_tree([1,2,3,4,5,6]))


