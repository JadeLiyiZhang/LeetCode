class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = [0] * 26
        for char in s:
            table[ord(char) - ord('a')] += 1
        for char in t:
            if table[ord(char) - ord('a')] == 0:
                return False
            table[ord(char) - ord('a')] -= 1
        return True