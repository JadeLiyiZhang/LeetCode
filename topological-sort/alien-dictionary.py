class Solution:
    def alienOrder(self, words: List[str]) -> str:
        parent, children = {}, {}
        count = {}
        for c in words[0]:
            parent[c] = set()
            children[c] = set()
        for i in range(1, len(words)):
            old, new = words[i - 1], words[i]
            j = 0
            while j < len(old) and j < len(new):
                if old[j] == new[j]:
                    j += 1
                else:
                    break
            if j == len(new) and j < len(old):
                return ""
            if j < len(old):
                if new[j] not in parent:
                    parent[new[j]] = set()
                    children[new[j]] = set()
                for c in parent[old[j]]:
                    if c == new[j]:
                        return ""
                    parent[new[j]].add(c)
                    children[c].add(new[j])
                parent[new[j]].add(old[j])
                children[old[j]].add(new[j])
                j += 1
            while j < len(new):
                if new[j] not in parent:
                    parent[new[j]] = set()
                    children[new[j]] = set()
                j += 1
        res = ""
        while len(parent) > 0:
            delete = []
            for c in parent:
                if len(parent[c]) == 0:
                    res += c
                    for ch in children[c]:
                        parent[ch].discard(c)
                    delete.append(c)
            for c in delete:
                del parent[c]
        return res