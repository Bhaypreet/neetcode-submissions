class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxele = 0
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                maxele = nums[i]
                cnt+=1
            else:
                if nums[i] != maxele:
                    cnt-=1
                if nums[i] == maxele:
                    cnt+=1

        return maxele