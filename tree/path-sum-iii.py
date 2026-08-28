# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hash_map = {0: 1}
        
        def backtrack(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = hash_map.get(curr_sum - targetSum, 0)
            hash_map[curr_sum] = hash_map.get(curr_sum, 0) + 1
            count += backtrack(node.left, curr_sum)
            count += backtrack(node.right, curr_sum)
            hash_map[curr_sum] -= 1
            return count
        return backtrack(root, 0)
