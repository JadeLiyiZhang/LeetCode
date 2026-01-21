class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        lst=[]
        for i in range(len(nums)):
            if i%10==nums[i]:
               lst.append(i)
        if len(lst)>=1:
            return min(lst)
        else:
            return -1