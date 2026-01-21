class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(string1):
            left, right = 0, len(string1) - 1
            while left < right:
                string1[left], string1[right] = string1[right], string1[left]
                left += 1
                right -= 1
            return string1
        
        list_res = list(s)
        for curr in range(0, len(s), 2 * k):
            list_res[curr: curr + k] = reverse(list_res[curr: curr + k])
        return ''.join(list_res)