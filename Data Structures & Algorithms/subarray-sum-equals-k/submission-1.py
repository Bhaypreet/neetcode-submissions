class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        pre = 0
        lis = 0
        for i in range(len(nums)):
            pre = pre+nums[i]
            a = pre-k
            if a in prefix :
                lis+=prefix[a]
            if pre in prefix:
                prefix[pre]+=1
            else:
                prefix[pre] = 1

        return lis