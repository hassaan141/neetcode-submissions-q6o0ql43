# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False

        res = []
        self.inOrderTraversal(root, res)

        prev = res[0]
        print(res)
        for i in range(1, len(res)):

            if res[i] > prev:
                prev = res[i]
                continue
            else:
                return False
        
        return True



    
    def inOrderTraversal(self, root, res):

        if root is None:
            return

        self.inOrderTraversal(root.left, res)
        res.append(root.val)
        self.inOrderTraversal(root.right, res)



        