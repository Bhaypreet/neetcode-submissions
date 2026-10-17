class Solution:
    def f(self,s1,s2,s3,i,j,dp):
        if i == len(s1) and j == len(s2):
            return True
        
        k = i+j
        if dp[i][j] != -1:
            return dp[i][j]

        if i < len(s1) and s1[i] == s3[k]:
            dp[i][j] = self.f(s1,s2,s3,i+1,j,dp)
            if dp[i][j]:
                return True
        if j < len(s2) and s2[j] == s3[k]:
            dp[i][j] = self.f(s1,s2,s3,i,j+1,dp)
            if dp[i][j] :
                return True
        
        return False
         
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        dp = [[-1 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

        if len(s1)+len(s2) != len(s3):
            return False
        return self.f(s1,s2,s3,0,0,dp)
           