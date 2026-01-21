class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) {
            return nums.length;
        }
        int write_p = 2;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[write_p - 2]) {
                nums[write_p] = nums[i];
                write_p++;
            } 
        }
        return write_p;
        }
    }