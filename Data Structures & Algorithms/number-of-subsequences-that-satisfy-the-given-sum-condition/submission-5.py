class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]+nums[j] <= target:
                    if i == j:
                        ans+=1
                    else:
                        ans+= 2**(j-i-1)
                else:
                    break

        return ans%(10**9 + 7)