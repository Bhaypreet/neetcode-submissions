class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        j = 0
        l = 0
        while(j < len(spaces)):
            if l == spaces[j]:
                ans+=" "
                j+=1
            ans+=s[l] 
            l+=1

        return ans+s[l:]

