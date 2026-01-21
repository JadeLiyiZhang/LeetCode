class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        max_flower = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                max_flower = 1
            else:
                max_flower = 0
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                max_flower += 1

            for i in range(1, len(flowerbed) - 1):
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1 
                    max_flower += 1
            
            if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                max_flower += 1

        if max_flower >= n:
            return True
        else:
            return False