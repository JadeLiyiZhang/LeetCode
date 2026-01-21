class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}
        for char1, char2 in zip(s, t):
            if (char1 not in mapping_s_t) and (char2 not in mapping_t_s):
                mapping_s_t[char1] = char2
                mapping_t_s[char2] = char1
            elif (mapping_s_t.get(char1, 0) != char2) or (mapping_t_s.get(char2, 0) != char1):
                return False
        return True