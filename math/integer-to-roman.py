class Solution:
    def intToRoman(self, num: int) -> str:
        arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        str_arr = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = []

        for i in range(len(arr)):
            if num == 0:
                break

            times = num // arr[i]
            res.extend([str_arr[i]] * times)
            num = num % arr[i]
        return ''.join(res)