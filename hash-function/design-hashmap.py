class ListNode:
    def __init__(self, key, val, next):
        self.val = val
        self.next = next
        self.key = key

class MyHashMap:

    def __init__(self):
        self.bucket = [None for _ in range(2048)]
        self.hash_num = len(self.bucket)
        

    def put(self, key: int, value: int) -> None:
        pos = key % self.hash_num
        head = self.bucket[pos]
        cur = head
        while cur:
            if cur.key == key:
                cur.val = value
                return
            cur = cur.next
        newNode = ListNode (key, value, head)
        self.bucket[pos] = newNode

    def get(self, key: int) -> int:
        pos = key % self.hash_num
        head = self.bucket[pos]
        cur = head
        while cur:
            print(cur.val)
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        pos = key % self.hash_num
        head = self.bucket[pos]
        dummy = ListNode(0, 0, head)
        cur = dummy
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                self.bucket[pos] = dummy.next
                return
            cur = cur.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)