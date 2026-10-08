class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in dic:
                return False
            else:
                dic[t[i]] -=1
                if dic[t[i]] == 0:
                    del dic[t[i]]
        return True
