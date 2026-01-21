class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
            end = max(end, last_occurrence[s[i]])
            if i == end:
                length = end - start + 1
                res.append(length)
                start = end + 1
        
        return res
