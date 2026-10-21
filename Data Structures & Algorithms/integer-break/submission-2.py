class Solution:
    def f(self,target,i):
        if target == 0:
            return 1
        if target < 0 or i > target:
            return 0
             

        take = self.f(target-i,i)*i
        nottake = self.f(target,i+1)

        return max(take,nottake)

    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1

        return self.f(n,1)