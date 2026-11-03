class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = 1
        b = 1
        pre = []
        suf = []

        for i in range(len(nums)):
            a = a*nums[i]
            pre.append(a)
            if a == 0:
                a = 1

        for i in range(len(nums)-1,-1,-1):
            b = b*nums[i]
            suf.append(b)
            if b == 0:
                b = 1

        suf = suf[::-1]

        maxi = float('-inf')
        for i in range(len(nums)):
            maxi = max(maxi,pre[i],suf[i])

        return maxi