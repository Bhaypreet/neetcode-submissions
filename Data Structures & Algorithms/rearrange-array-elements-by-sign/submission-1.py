class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = 0
        r = 0
        while(l < len(nums) and r < len(nums)):
            if l %2 ==0 :
                if nums[l] > 0:
                    l+=1
                    r=l
                else:
                    while(nums[r]< 0):
                        r+=1
                    a = nums.pop(r)
                    nums.insert(l,a)
                    r = l
            else:
                if nums[l] < 0 :
                    l+=1
                    r= l

                else:
                    while(nums[r] > 0):
                        r+=1
                    a = nums.pop(r)
                    nums.insert(l,a)
                    r=l

        return nums