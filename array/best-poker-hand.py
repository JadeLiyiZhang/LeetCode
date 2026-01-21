class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        flush = True
        for i in range(1, len(suits)):
            if suits[i] != suits[i-1]:
                flush = False
        
        three_of_kind = True
        pair = True
        store = {}
        for j in range(len(ranks)):
            if ranks[j] not in store:
                store[ranks[j]] = 1
            else:
                store[ranks[j]] += 1
        
        store = sorted(store.items(), key=lambda x:x[1], reverse=True)
        if store[0][1] < 3:
            three_of_kind = False
        
        if store[0][1] < 2:
            pair = False
        
        if flush == True:
            return 'Flush'
        
        elif three_of_kind == True:
            return 'Three of a Kind'
        
        elif pair == True:
            return 'Pair'

        else:
            return 'High Card'