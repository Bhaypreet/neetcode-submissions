class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        mini = min(strs,key=len)
        for i in range(len(mini)):
            a = strs[0][i]
            for items in strs:
                if items[i] != a:
                    return ans
            ans+=strs[0][i]

        return ans