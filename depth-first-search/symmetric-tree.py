# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if left and not right:
                return False
            if right and not left:
                return False
            if right and left and right.val != left.val:
                return False
            if not left and not right:
                return True
            return helper(left.left, right.right) and helper(left.right, right.left)
        return helper(root.left, root.right)