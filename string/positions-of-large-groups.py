class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        startIndex = 0
        n = len(s)

        for i in range(1, n + 1):  # 将遍历扩展到字符串长度+1，以便能处理最后一个字符组
            # 检查当前字符是否不同于前一个或已达到字符串末尾
            if i == n or s[i] != s[startIndex]:
                # 如果当前字符组长度大于等于3，则记录其起始和结束索引
                if i - startIndex >= 3:
                    res.append([startIndex, i - 1])
                startIndex = i  # 更新开始索引

        return res