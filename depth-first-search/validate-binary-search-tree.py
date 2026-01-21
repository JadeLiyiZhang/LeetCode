# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, left_bound, right_bound):
            if not node:
                return True
            if node.val <= left_bound or node.val >= right_bound:
                return False
            return helper(node.left, left_bound, node.val) and helper(node.right, node.val, right_bound)
        
        return helper(root, float('-inf'), float('inf'))
            