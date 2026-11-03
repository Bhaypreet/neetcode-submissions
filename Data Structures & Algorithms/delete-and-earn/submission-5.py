class Solution:
    def f(self,lis,i,dic):
        if i == len(lis):
            return 0

        a = lis[i]*dic[lis[i]]
        if i+1 < len(lis) and lis[i+1] == lis[i]+1:
            
            pick = a+self.f(lis,i+2,dic)
            notp = self.f(lis,i+1,dic)

            return max(pick,notp)
        
        else:
            pick = a+self.f(lis,i+1,dic)
            notp = self.f(lis,i+1,dic)
            return max(pick,notp)

    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]] += 1

        lis = sorted(dic.keys())
        return self.f(lis,0,dic)