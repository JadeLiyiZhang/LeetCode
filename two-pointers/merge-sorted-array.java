class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int cur1 = m - 1;
        int cur2 = n - 1;
        int p = m + n - 1;

        while (cur1 >= 0 && cur2 >= 0) {
            if (nums1[cur1] >= nums2[cur2]) {
                nums1[p] = nums1[cur1];
                cur1--;
            } else {
                nums1[p] = nums2[cur2];
                cur2--;
            }
            p--;
        }
        
        while (cur2 >= 0) {
            nums1[p] = nums2[cur2];
            p--;
            cur2--;
        }
    }
}