class Solution:
    def findComplement(self, num: int) -> int:
        def decimal_to_binary(n):
            if n == 0:
                return '0'
            binary = ''
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary
        
        def binary_to_decimal(binary_str):
            decimal = 0
            binary_str = binary_str[::-1]
            for i in range(len(binary_str)):
                decimal += int(binary_str[i]) * 2 ** i
            return decimal
        
        temp_bi = decimal_to_binary(num)
        reversed_bi = ''
        for _ in temp_bi:
            if _ == '0':
                reversed_bi += '1'
            elif _ == '1':
                reversed_bi += '0'
        return binary_to_decimal(reversed_bi)