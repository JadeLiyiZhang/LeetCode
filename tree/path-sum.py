# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False
        def helper(node, left):
            if not node or self.ans:
                return
            left -= node.val
            if not node.left and not node.right and left == 0:
                self.ans = True
                return
            helper(node.left, left)
            helper(node.right, left)
        helper(root, targetSum)
        if self.ans:
            return True
        return False