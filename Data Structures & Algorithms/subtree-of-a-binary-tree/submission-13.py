# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root and not subRoot: 
            return True

        
        stack = [ root ]
        traversed = False
        while stack:
            node = stack.pop()

            if node.val == subRoot.val:
                traversed = self.isSimilarTree(node, subRoot)
                if traversed:
                    return True
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)

        return False

    def isSimilarTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):

        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSimilarTree(p.right, q.right) and self.isSimilarTree(p.left, q.left)
        
        return False
        