class Solution:
    def maxDifference(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]]+=1
        lis1 = []
        lis2 = []

        for key,value in dic.items():
            if value %2 == 0:
                lis1.append(value)
            else:
                lis2.append(value)

        return max(lis2) - min(lis1)