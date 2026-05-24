# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        queue, result = [root], []
        level_size = 1

        while queue:
            cur_node = queue.pop(0)

            if result == []:
                result.append([cur_node.val])
            else:
                if len(result[-1]) == level_size:
                    level_size = len(queue) + 1
                    result.append([cur_node.val])
                else:
                    last_level = result.pop()
                    last_level.append(cur_node.val)
                    result.append(last_level)

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        return result