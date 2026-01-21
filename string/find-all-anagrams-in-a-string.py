class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        list_s = [0] * 26
        list_p = [0] * 26
        res = []
        
        for i in range(len(p)):
            list_s[ord(s[i]) - ord('a')] += 1
            list_p[ord(p[i]) - ord('a')] += 1
        
        if list_s == list_p:
            res.append(0)
        
        for i in range(len(s) - len(p)):
            list_s[ord(s[i]) - ord('a')] -= 1
            list_s[ord(s[i + len(p)]) - ord('a')] += 1

            if list_s == list_p:
                res.append(i + 1)
        
        return res