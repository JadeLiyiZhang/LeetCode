class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        for i in range(len(fruits)):
            res = 1
            basket_1 = fruits[i]
            basket_2 = None
            for j in range(i + 1, len(fruits)):
                if fruits[j] == basket_1:
                    res += 1
                elif basket_2 is None:
                    basket_2 = fruits[j]
                    res += 1
                elif fruits[j] == basket_2:
                    res += 1
                else:
                    break
            ans = max(res, ans)
        return ans