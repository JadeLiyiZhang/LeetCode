from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number = number * 10 + digit
        number += 1
        array = [0] * len(str(number))
        for i in range(len(str(number)) - 1,-1,-1):
            array[i] = number % 10
            number //= 10
        return array

