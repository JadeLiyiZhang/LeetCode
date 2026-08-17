# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return True
            if node.left and node.left.val > node.val:
                return False
            if node.right and node.right.val < node.val:
                return False
            return helper(node.left) and helper(node.right)
        return helper(root)