# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {val: i for i, val in enumerate(inorder)}
        def helper(in_start, in_end):
            if in_start > in_end:
                return None
            root_val = preorder.pop(0)
            root_node = TreeNode(root_val)

            in_pos = in_map[root_val]
            root_node.left = helper(in_start, in_pos - 1)
            root_node.right = helper(in_pos + 1, in_end)
            return root_node
        return helper(0, len(inorder) - 1)
