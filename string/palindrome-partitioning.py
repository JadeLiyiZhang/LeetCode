class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(left, right):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        res = []
        path = []
        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()
        backtrack(0)
        return res