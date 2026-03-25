class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_to_t = {}
        mapping_t_to_s = {}
        for char1, char2 in zip(s, t):
            # store the mapping in both dic
            if char1 not in mapping_s_to_t and char2 not in mapping_t_to_s:
                mapping_s_to_t[char1] = char2
                mapping_t_to_s[char2] = char1
            else:
                if mapping_s_to_t.get(char1, 0) != char2 or mapping_t_to_s.get(char2, 0) != char1:
                    return False
        return True