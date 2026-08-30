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
            if node.val > highest or node.val < lowest:
                return False
            else:
                if node.left:
                    validation(node.left, node.val, lowest)
                if node.right:
                    validation(node.right, highest, node.val)
            return True
        return validation(root.left, root.val, float('-inf')) and validation(root.right, float('inf'), root.val)