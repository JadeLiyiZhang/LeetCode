# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        remaining = []

        def helper(node):
            if not node:
                return None
            node.left = helper(node.left)
            node.right = helper(node.right)
            if node.val in to_delete_set:
                if node.left:
                    remaining.append(node.left)
                if node.right:
                    remaining.append(node.right)
                return None
            return node

        # Start the recursion from the root
        root = helper(root)
        # If root is not deleted, add it to the result
        if root:
            remaining.append(root)
        return remaining
