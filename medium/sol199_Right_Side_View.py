from stuff import *
class Solution:
    def rightSideView(self, root) :
        rv = []

        def dfs2(node,level):
            if not node:
                return
            if len(rv) == level:
                rv.append(node.val)
            dfs2(node.right,level+1)
            dfs2(node.left, level + 1)


        dfs2(root,0)
        return rv

class Solution2:
    def rightSideView(self,root):
        rv = []
        q = []
        q.append(root)
        while len(q) != 0:
            l = len(q)
            for i in range(l):
                n = q.pop(0)
                if i == 0:
                    rv.append(n.val)
                if not n.right:
                    q.append(n.right)
                if not n.left :
                    q.append(n.left)
        return rv

if __name__ == '__main__':
    t = createTree([1,2,3,None,5,None,4])
    t2 = createTree([1,2])
    t3 = createTree([1,2,3,4])

    print(Solution().rightSideView(t3))


