class Solution:
    def frequencySort(self, s: str) -> str:
        dict = {}
        res = ''
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        dict_freq = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        for val, num in dict_freq:
            res += val * num
        return res
