class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = nums[0]
        b = nums[-1]
        pre = [a]
        suffix = [b]
        ans = float('-inf')


        for i in range(1,len(nums)):
            if a == 0:
                a = 1
            a = a*nums[i]
            pre.append(a)

        for i in range(len(nums)-2,-1,-1):
            if b == 0:
                b = 1
            b =b*nums[i] 
            suffix.append(b)

        suf = suffix[::-1]

        for i in range(len(nums)):
            ans = max(ans,suf[i],pre[i])

        return ans

