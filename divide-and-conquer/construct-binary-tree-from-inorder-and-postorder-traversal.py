# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for index, val in enumerate(inorder):
            inorder_map[val] = index

        def helper(left, right):
            if left > right:
                return
            root_val = postorder.pop()
            root_index = inorder_map[root_val]
            root = TreeNode(root_val)
            root.right = helper(root_index + 1, right)
            root.left = helper(left, root_index - 1)
            return root

        return helper(0, len(inorder) - 1)

