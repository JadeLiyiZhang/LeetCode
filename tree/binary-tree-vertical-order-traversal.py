# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        map = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, k = queue.popleft()
            map[k].append(node.val)
            if node.left:
                queue.append((node.left, k - 1))
            if node.right:
                queue.append((node.right, k + 1))
        return [map[k] for k in sorted(map.keys())]