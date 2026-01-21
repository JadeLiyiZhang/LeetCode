class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = []
        nums.append(0)
        nums.append(1)
        for i in range(2,n+1):
            if i%2==0:
                nums.append(nums[i//2])
            else:
                nums.append(nums[i//2] + nums[(i//2) + 1])
        if n==0:
            return 0
        return max(nums)
