class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        storage = {}
        ans = 0
        for right in range(len(fruits)):
            fruit_right = fruits[right]
            storage[fruit_right] = storage.get(fruit_right, 0 ) + 1
            while len(storage) > 2:
                fruit_left = fruits[left]
                storage[fruit_left] -= 1
                if storage[fruit_left] == 0:
                    del storage[fruit_left]
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans 
