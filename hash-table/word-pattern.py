class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_pattern_to_s = {}
        map_s_to_pattern = {}
        list_s = s.split(" ")
        if len(pattern) != len(list_s):
            return False
        for char, word in zip(pattern, list_s):
            if char in map_pattern_to_s:
                if map_pattern_to_s[char] != word:
                    return False
            if word in map_s_to_pattern:
                if map_s_to_pattern[word] != char:
                    return False
            if (word not in map_s_to_pattern) and (char not in map_pattern_to_s):
                map_pattern_to_s[char] = word
                map_s_to_pattern[word] = char
        return True
