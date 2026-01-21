class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for str_ in strs:
            one_num = self.getOne(str_)
            zero_num = self.getZero(str_)
            for i in range(n, one_num - 1, -1):
                for j in range(m, zero_num - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - one_num][j - zero_num] + 1)
        return dp[n][m]
        
    def getZero (self, str_):
        zero_num = 0
        for char in str_:
            if char == '0':
                zero_num += 1
        return zero_num
    
    def getOne(self, str_):
        one_num = 0
        for char in str_:
            if char == '1':
                one_num += 1
        return one_num