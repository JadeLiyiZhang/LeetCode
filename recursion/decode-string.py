class Solution:
    def decodeString(self, s: str) -> str:
        cur_s = ''
        cur_num = 0
        stack = []
        for char in s:
            if char.isdigit():
                cur_num = char * 10 + cur_num
            if char.isalpha():
                cur_s += char
            if char == '[':
                stack.append((cur_s, cur_num))
                cur_num = 0
                cur_s = ''
            if char == ']':
                s, num = stack.pop()
                cur_s = s + cur_s * num
        return cur_s