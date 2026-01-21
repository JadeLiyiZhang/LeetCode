class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(left, right, nums):
            head, tail = left, right - 1
            while head < tail:
                nums[head], nums[tail] = nums[tail], nums[head]
                head += 1
                tail -= 1
        
        n = len(nums)
        rotate_times = k % n
        left_part = n - rotate_times
        reverse(0, left_part, nums)
        reverse(left_part, n, nums)
        reverse(0, n, nums)