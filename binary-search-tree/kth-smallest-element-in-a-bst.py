# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = self.count(root.left)
        if num == k - 1:
            return root.val
        if num >= k:
            return self.kthSmallest(root.left, k)
        return self.kthSmallest(root.right, k - 1 - num)

    def count(self, node):
        if node is None:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)