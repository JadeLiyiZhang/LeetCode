class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        table = {}
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (nums1[i] + nums2[j]) not in table:
                    table[nums1[i] + nums2[j]] = 1
                else:
                    table[nums1[i] + nums2[j]] += 1

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                target = -(nums3[i] + nums4[j])
                if target in table:
                    res += table[target]
        
        return res
