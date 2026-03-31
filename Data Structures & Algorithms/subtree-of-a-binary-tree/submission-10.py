# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:   
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

#         if root is None and subRoot is None:
#             return True
#         elif root is None and subRoot is not None:
#             return False
#         elif root is not None and subRoot is None:
#             return True

#         stack = [root]
#         output = False
#         while len(stack) > 0:

#             node = stack.pop()

#             if node.val == subRoot.val:
#                 print(f"node.val is {node.val} and {subRoot.val}")
#                 output = self.isSameTree(node, subRoot)
#                 if output:
#                     return True
        
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return output
    
#     def isSameTree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        
#         if not r and not s:
#             return True
        
#         if r and s and r.val == s.val:
#             return self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right)
#         else:
#             return False



class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is not None:
            return False
        elif root is not None and subRoot is None:
            return True

        stack = [root]
        output = False
        while len(stack) > 0:

            node = stack.pop()

            if node.val == subRoot.val:
                output = self.isSameTree(node, subRoot)
                if output:
                    return True
        
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return output
    
    def isSameTree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        
        if not r and not s:
            return True
        
        if r and s and r.val == s.val:
            return self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right)
        else:
            return False




        


        