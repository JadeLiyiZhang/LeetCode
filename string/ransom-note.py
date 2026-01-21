class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for char in magazine:
            dic[char] = dic.get(char, 0) + 1
        for i in ransomNote:
            if i not in dic or dic[i] == 0:
                return False
            else:
                dic[i] -= 1
        return True
