# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        l = []
        def in_order(root: Optional[TreeNode]):
            
            if root is None:
                return

            in_order(root.left)
            l.append(root.val)
            in_order(root.right)
        
        in_order(root)

        first = l[0]
        for i in range(1, len(l)):  

            if l[i] > first:
                first = l[i]
            else:
                return False
        
        return True

           





            


        
        