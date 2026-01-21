class Solution {
    public int removeElement(int[] nums, int val) {
        int p = 0;
        int last = nums.length - 1;
        int res = 0;
        while (p <= last) {
            if (nums[p] != val) {
                p++;
                res++;
            } else {
                int temp = nums[p];
                nums[p] = nums[last];
                nums[last] = temp;
                last--;
            }
        }
        return res;
    }
}