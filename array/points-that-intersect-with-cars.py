class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        set_car = set()
        for num in nums:
            for _ in range(num[0], num[1] + 1):
                set_car.add(_)
        
        return len(set_car)
