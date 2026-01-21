class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double_s = s + s
        double_s = double_s[1:len(double_s) - 1]
        if s in double_s:
            return True
        
        return False