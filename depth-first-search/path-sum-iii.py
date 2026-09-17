# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        table = {0: 1}
        count = 0
        def dfs(node, cur_sum):
            nonlocal count
            if not node:
                return 0
            cur_sum += node.val
            count += table.get(cur_sum - targetSum, 0)
            table[cur_sum] = table.get(cur_sum, 0) + 1
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            table[cur_sum] -= 1
        dfs(root, 0)
        return count