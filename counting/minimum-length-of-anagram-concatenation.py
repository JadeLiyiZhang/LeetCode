class Solution:
    def minAnagramLength(self, s: str) -> int:
        stringList = list(s)
        n = len(s)
        for size in range(1, n):
            if n % size == 0:
                initialList = sorted(stringList[:size])
                for j in range(size, n, size):
                    temp = stringList[j:j+size]
                    temp.sort()

                    if initialList != temp:
                        break
                else:
                    return size

        return n