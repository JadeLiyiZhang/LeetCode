class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ''
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res