class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        ans = []
        for ch in order:
            if ch in dic:
                ans.append(ch*dic[ch])
                del dic[ch]

        for key,value in dic.items():
            ans.append(key*value)
        
        ans = "".join(ans)
        return ans