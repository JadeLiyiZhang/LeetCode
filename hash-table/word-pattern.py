class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping_pattern_to_s = {}
        mapping_s_to_pattern = {}
        s = s.split()
        for char, word in zip(pattern, s):
            print(char, word)
            if char not in mapping_pattern_to_s and word not in mapping_s_to_pattern:
                mapping_pattern_to_s[char] = word
                mapping_s_to_pattern[word] = char
            else:
                if mapping_pattern_to_s.get(char, 0) != word or mapping_s_to_pattern.get(word, 0) != char:
                    return False
        return True