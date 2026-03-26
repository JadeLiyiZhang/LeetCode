from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for word in strs:
            pattern = [0] * 26
            for char in word:
                pattern[ord(char) - ord('a')] += 1
            table[tuple(pattern)].append(word)
        res = []
        for key in table:
            values = table[key]
            res.append(values)
        return res
            