class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(n):
            left, right = 0, len(n) - 1
            while left < right:
                n[left], n[right] = n[right], n[left]
                left += 1
                right -= 1
            return n
        
        list_s = s.split()
        return ' '.join(reverse(list_s))