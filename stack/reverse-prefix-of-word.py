class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ''
        index = 0
        if ch not in word:
            return word

        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break
            
        for i in range(i+1):
            res = word[i] + res
        
        for i in range(index + 1, len(word)):
            res += word[i]

        return res

