class Solution:
    def myAtoi(self, s: str) -> int:
        indexStart, indexEnd = -1, -1
        result = 0
        if len(s)==1 and not s[0].isdigit():
            return 0
        for i in range(len(s)):
            if (s[i]=="+" or s[i]=="-"):
                if indexStart!=-1:
                    if indexEnd==-1:
                        return 0
                    else:
                        break
                indexStart = i
            elif s[i].isdigit():
                if indexStart==-1:
                    indexStart=i
                indexEnd = i
            else:
                if indexStart==-1 and s[i]!=' ':
                    return result
                elif indexEnd>-1:
                    break
                elif indexStart!=-1 and indexEnd==-1:
                    return 0
                else:
                    pass
        if indexStart==-1 or indexEnd==-1:
            return 0
        elif indexStart==indexEnd:
            return int(s[indexStart])
        result = int(s[indexStart:indexEnd+1])
        if result < -2**31:
            return -2**31
        elif result > (2**31) - 1:
            return (2**31) - 1
        return result