class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        g_cur = 0
        s_cur = 0
        while g_cur < len(g) and s_cur < len(s):
            if s[s_cur] >= g[g_cur]:
                g_cur += 1
                s_cur += 1
                res += 1
            else:
                s_cur += 1
        return res