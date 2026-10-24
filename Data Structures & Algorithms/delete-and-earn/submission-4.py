class Solution:
    def f(self, nums, dic, i, dp):
        if i >= len(nums):
            return 0

        if i in dp:
            return dp[i]

        take = nums[i] * dic[nums[i]]

        if i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            take += self.f(nums, dic, i + 2, dp)
        else:
            take += self.f(nums, dic, i + 1, dp)

        nottake = self.f(nums, dic, i + 1, dp)

        dp[i] = max(take, nottake)
        return dp[i]

    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = {}

        for x in nums:
            dic[x] = dic.get(x, 0) + 1

        arr = sorted(dic.keys())
        dp = [-1] * len(arr)

        return self.f(arr, dic, 0, dp)