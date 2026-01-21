from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_pattern = defaultdict(list)
        for word in strs:
            pattern = [0] * 26
            for char in word:
                pattern[ord(char) - ord('a')] += 1

            group_pattern[tuple(pattern)].append(word)
        return list(group_pattern.values())
