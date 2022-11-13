import sys
sys.path.append("/Users/charlesphillips/leet_code_python")
for m in sys.path:
    print(m)


from stuff.tree_stuff import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None
        lower, upper = p,q if p.val < q.val else q,p
        def helper(node):
            nonlocal lca
            if node is None:
                return 
            if node.val == lower.val or node.val == upper.val:
                return lower
            if lower.val < node.val < upper.val:
                lca = node.val
                return
            
            if (lower.val < upper.val <  node.val):
                helper(node.left)
            if node.val < lower.val < upper.val:
                helper(node.right)
        
        helper(root)
        return lca
        


            

            
                
if __name__ == "__main__":
    
    tree = TreeNode.list_to_tree([6,2,8,0,4,7,9,None,None,3,5])
    print(Solution().lowestCommonAncestor(tree,TreeNode(val=2), TreeNode(val=8)))


    # if search(node.l,node.r): node.val is the LCA
