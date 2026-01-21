class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_Num = list(str(n))
        for i in range(len(str_Num) - 1, 0, -1):
            if int(str_Num[i - 1]) > int(str_Num[i]):
                str_Num[i - 1] = str(int(str_Num[i - 1]) - 1)
                for j in range(i, len(str_Num)):
                    str_Num[j] = '9'
        return int(''.join(str_Num))