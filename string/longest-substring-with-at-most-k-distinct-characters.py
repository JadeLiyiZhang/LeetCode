class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        map = {}
        left = 0
        count = 0
        ans = 0
        for right in range(len(s)):
            print(map)
            if s[right] not in map:
                count += 1
                map[s[right]] = map.get(s[right], 0) + 1
                while count > k:
                    map[s[left]] -= 1
                    if map[s[left]] == 0:
                        count -= 1
                        del map[s[left]]
                    left += 1
            else:
                map[s[right]] += 1
            ans = max(ans, right - left + 1)
        return ans