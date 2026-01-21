class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) < 2 or stones[1] != 1:
            return False

        #key: stone position
        #value: set of jump length that can reach the stone
        dp = {stone: set() for stone in stones}
        dp[stones[0]].add(0)

        for stone in stones:
            for k in dp[stone]:
                for step in (k - 1, k, k + 1):
                    if step > 0 and (stone + step) in dp:
                        dp[stone + step].add(step)
        
        return bool(dp[stones[-1]])