class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = [0] * 26
        for char in s:
            store[ord(char) - ord('a')] += 1

        for char in t:
            store[ord(char) - ord('a')] -= 1

        for num in store:
            if num != 0:
                return False

        return True
