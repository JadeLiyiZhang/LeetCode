# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validation(node, highest, lowest):
            if not node:
                return True
            if node.val >= highest or node.val <= lowest:
                return False
            return validation(node.left, node.val, lowest) and validation(node.right, highest, node.val)
        return validation(root, float('inf'), float('-inf'))