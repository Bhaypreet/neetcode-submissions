class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = k-1
        ans = float('inf')
        while(r < len(nums)):
            maxi = max(nums[l:r+1])
            mini = min(nums[l:r+1])
            ans = min(ans,maxi-mini)
            l+=1
            r+=1

        return ans