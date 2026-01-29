class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word):
            word_list = list(word)
            left, right = 0, len(word) - 1
            while left < right:
                word_list[left], word_list[right] = word_list[right], word_list[left]
                left += 1
                right -= 1
            return ''.join(word_list)
        
        reversed_s = reverse(s.strip())
        res = []
        for word in reversed_s.split():
            word = reverse(word)
            res.append(word)
        return ' '.join(res)