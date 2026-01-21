class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        longest_word = ''
        for word in dictionary:
            i = 0
            j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(word):
                if len(longest_word) < i:
                    longest_word = word
                elif len(longest_word) == i:
                    longest_word = min(longest_word, word)
        return longest_word

