# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if q is not None and p is None:
            return False
        elif q is None and p is not None:
            return False
        elif q is None and p is None:
            return True
        elif q.val != p.val:    
            return False

        print(p.val)
        print(q.val)


        right = self.isSameTree(p.right, q.right)
        left = self.isSameTree(p.left, q.left)

        if right and left:
            return True
        else:
            return False
               



        
        

        