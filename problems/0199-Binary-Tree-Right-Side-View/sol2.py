# ==========================================================
# 199. Binary Tree Right Side View
# Difficulty : Medium
# Language   : Python
# Solution   : #2
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.2 MB (Beats 93%)
# Link       : https://leetcode.com/problems/binary-tree-right-side-view/
# ==========================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level_len = len(q)
            for i in range(len(q)):
                cur_node = q.popleft()
                if i == level_len - 1:
                    res.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
        return res