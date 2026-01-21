# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.helper(root, low, high)
    
    def helper(self, node, low, high):
        if node is None:
            return 0
        current_val = 0
        if low <= node.val <= high:
            current_val += node.val
        left_sum = self.helper(node.left, low, high)
        right_sum = self.helper(node.right, low, high)
        return current_val + left_sum + right_sum