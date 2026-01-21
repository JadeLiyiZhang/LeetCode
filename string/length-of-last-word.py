class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        last_count = 0
        s = s.strip()
        for i in range(len(s)):
            if s[i] != ' ':
                count += 1
            else:
                if s[i - 1] != ' ':
                    count = 0
                else:
                    continue
        return count

            