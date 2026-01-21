class Node:
    def __init__(self):
        self.next = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.next:
                cur.next[ch] = Node()
            cur = cur.next[ch]
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.next:
                return False
            cur = cur.next[ch]
        if cur.end != True:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.next:
                return False
            cur = cur.next[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)