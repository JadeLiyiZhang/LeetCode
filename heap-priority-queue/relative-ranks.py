class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {}
        res = []
        copy_score = copy.deepcopy(score)
        score_rank = sorted(copy_score, reverse=True)
        for i in range(len(score)):
            rank[score[i]] = score_rank.index(score[i])
        for i in range(len(score)):
            if rank[score[i]] == 0:
                res.append('Gold Medal')
            elif rank[score[i]] == 1:
                res.append('Silver Medal')
            elif rank[score[i]] == 2:
                res.append('Bronze Medal')
            else:
                res.append(str(rank[score[i]] + 1))
        
        return res