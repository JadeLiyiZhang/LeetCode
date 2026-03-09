class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s or not t:
            return True
        pointer = 0
        for char in t:
            if char == s[pointer]:
                pointer += 1
            if pointer == len(s):
                return True

        return False