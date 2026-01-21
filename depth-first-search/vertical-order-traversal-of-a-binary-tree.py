# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def insert(val, maplist, k):
            i, j = len(maplist) - k, len(maplist) - 1
            while i <= j:
                mid = (i + j) // 2
                if maplist[mid] >= val:
                    j -= 1
                else:
                    i += 1
            maplist.insert(i, val)
            
        if not root:
            return []

        vertical = defaultdict(list)
        same = defaultdict(int)
        queue = deque([(root, 0, 0)])
        while queue:
            node, h, v = queue.popleft()
            insert(node.val, vertical[v], same[(h, v)])
            same[(h, v)] += 1
            if node.left:
                queue.append((node.left, h + 1, v - 1))
            if node.right:
                queue.append((node.right, h + 1, v + 1))
        return [vertical[v] for v in sorted(vertical.keys())]