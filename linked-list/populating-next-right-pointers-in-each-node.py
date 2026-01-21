from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        q = deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
            prev.next = None
        return root
