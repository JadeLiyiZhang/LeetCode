class Node:

    def __init__(self):
        self.next = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.next:
                cur.next[ch] = Node()
            cur = cur.next[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.end
            ch = word[idx]
            if ch == '.':
                for child in node.next.values():
                    if dfs(child, idx + 1):
                        return True
                return False
            
            else:
                nxt = node.next.get(ch)
                if nxt is None:
                    return False
                return dfs(nxt, idx + 1)
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)