class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alpha = [0] * 26
        for char in magazine:
            alpha[ord(char) - ord('a')] += 1
        for char in ransomNote:
            if alpha[ord(char) - ord('a')] == 0:
                return False
            alpha[ord(char) - ord('a')] -= 1
        return True