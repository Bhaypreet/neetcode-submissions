class Solution:
    def cp(self,st):
        l = 0
        r = len(st)-1
        while(l <= r):
            if st[l] != st[r]:
                return False
            l+=1
            r-=1
        return True

    
    def f(self,s,i,lis,ans):
        if i == len(s):
            ans.append(lis[:])
            return

        for j in range(i, len(s)):
            st = s[i:j+1]

            if self.cp(st):
                lis.append(st)
                self.f(s, j+1, lis, ans)
                lis.pop()

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.f(s,0,[],ans)
        return ans