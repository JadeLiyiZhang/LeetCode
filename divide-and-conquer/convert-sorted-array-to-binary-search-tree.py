# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return
            mid = left + (right - left) // 2
            root_node = TreeNode(nums[mid])
            root_node.left = helper(left, mid - 1)
            root_node.right = helper(mid + 1, right)
            return root_node
        return helper(0, len(nums) - 1)