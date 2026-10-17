class Solution:
    def f(self,i,n,k,lis,ans):
        if len(lis) == k:
            ans.append(lis[:])
            return 

        if i > n:
            return 

        lis.append(i)
        self.f(i+1,n,k,lis,ans)
        lis.pop()
        self.f(i+1,n,k,lis,ans)

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.f(1,n,k,[],ans)
        return ans


        