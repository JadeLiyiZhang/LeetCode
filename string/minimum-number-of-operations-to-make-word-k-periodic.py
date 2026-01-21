class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        res = 0
        record = {}
        for i in range(0, len(word), k):
            record[word[i:i + k]] = record.get(word[i:i + k], 0) + 1
        
        record = sorted(record.items(), key=lambda item: item[1])
        
        for i in range(len(record) - 1):
            res += record[i][1]
        
        return res