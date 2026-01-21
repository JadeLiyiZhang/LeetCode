class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

        res = []
        def dfs(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for i in letterMap[int(digits[index])]:
                path.append(i)
                dfs(index+1, path)
                path.pop()
        if not digits:
            return []
        dfs(0, [])
        return res