class Solution:
    def f(self,n,o,c,s,ans):
        if o == n and c == n :
            ans.append(s)
            return

        if o > n or c > n:
            return

        if o > c :
            self.f(n,o+1,c,s+"(",ans)
            self.f(n,o,c+1,s+")",ans)
        else:
            self.f(n,o+1,c,s+"(",ans)

        return ans

    def generateParenthesis(self, n: int) -> List[str]:
        return self.f(n,0,0,"",[])