# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # 1. 均为空节点，对称
            if not left and not right:
                return True
            # 2. 只有一个为空，或节点值不相等，不对称
            if not left or not right or left.val != right.val:
                return False
            # 3. 递归比较外侧 (left.left, right.right) 与 内侧 (left.right, right.left)
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)