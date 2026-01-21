class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node


    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.deleteNode(node)
        self.addNode(node)
        self.cache[key] = self.head.next
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            newNode = Node(key, value)
            self.addNode(newNode)
            self.cache[key] = self.head.next
        else:
            if len(self.cache) == self.capacity:
                deletedNode = self.tail.prev
                self.deleteNode(self.tail.prev)
                del self.cache[deletedNode.key]
            newNode = Node(key, value)
            self.addNode(newNode)
            self.cache[key] = self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)