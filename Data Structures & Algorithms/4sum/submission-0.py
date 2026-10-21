class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                lis = []
                l = j+1
                r = len(nums)-1
                while(l < r):
                    a = nums[i]+nums[j]+nums[l]+nums[r]
                    if a == target:
                        lis = [nums[i],nums[j],nums[l],nums[r]]
                        lis.sort()
                        if lis not in ans:
                            ans.append(lis)
                        l+=1
                        r-=1
                    elif a > target:
                        r-=1
                    else:
                        l+=1

        return ans