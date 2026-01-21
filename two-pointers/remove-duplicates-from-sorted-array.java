class Solution {
    public int removeDuplicates(int[] nums) {
        int pos = 1;
        int cur = 1;
        while (cur < nums.length) {
            if (nums[cur] == nums[cur - 1]) {
                cur++;
            } else {
                nums[pos] = nums[cur];
                pos++;
                cur++;
            }
        }
        return pos;
    }
}