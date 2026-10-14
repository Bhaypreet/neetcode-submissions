class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lis = []
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while(l < r):
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0:
                    if (nums[i],nums[l],nums[r]) not in lis:
                        lis.append((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif sum > 0:
                    r-=1
                else:
                    l+=1
                
        return lis