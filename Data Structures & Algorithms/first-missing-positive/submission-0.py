class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lis = list(set(nums))
        lis.sort()
        k = 1
        i = 0
        while(i < len(lis) and lis[i] <= 0):
            i+=1
        if i == len(lis):
            return k
        
        for j in range(i,len(lis)):
            if lis[j] != k:
                return k
            else:
                k+=1

        return k

                