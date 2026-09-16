"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        res = []
        def dfs(node):
            if not node:
                return
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for child in node.children:
                dfs(child)
        dfs(root)
        print(','.join(res))
        return ','.join(res)
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        nodes = data.split(',')
        index = 0

        def dfs():
            nonlocal index
            node_val = nodes[index]
            index += 1
            num_children = int(nodes[index])
            index += 1

            node = Node(val=int(node_val), children = [])
            for i in range(num_children):
                child = dfs()
                node.children.append(child)
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))