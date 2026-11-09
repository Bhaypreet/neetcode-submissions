class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lis1 = s1.split()
        dic1 = {}
        for item in lis1 :
            if item not in dic1:
                dic1[item] = 1
            else:
                dic1[item] +=1

        lis2 = s2.split()

        dic2 = {}
        for item in lis2 :
            if item not in dic2:
                dic2[item] = 1
            else:
                dic2[item] +=1 

        

        ans =  []
        for i in range(len(lis1)):
            if lis1[i] not in lis2 and dic1[lis1[i]] == 1:
                if lis1[i] not in ans:
                    ans.append(lis1[i])

        for i in range(len(lis2)):
            if lis2[i] not in lis1 and dic2[lis2[i]] == 1:
                if lis2[i] not in ans:
                    ans.append(lis2[i])

        return ans 