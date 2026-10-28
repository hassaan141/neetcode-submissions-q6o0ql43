# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # This makes the p value always smaller than the q values which makes it easier
        if p.val > q.val: 
            tmp = q
            q = p 
            p = tmp
        
        print(p.val, q.val)

        if (p.val <= root.val and q.val > root.val) or (p.val < root.val and q.val >= root.val):
            return root
        
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)



        