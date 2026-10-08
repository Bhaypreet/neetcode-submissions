class Solution:
    def f(self, candidates, target, lis, ans, i):

        if sum(lis) == target:
            if lis not in ans:
                ans.append(lis.copy())
            return

        if i >= len(candidates) or sum(lis) > target:
            return

        
        # Take
        lis.append(candidates[i])
        self.f(candidates, target, lis, ans, i + 1)
        lis.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1

        # Not take
        self.f(candidates, target, lis, ans, i + 1)

    def combinationSum2(self, candidates, target):
        ans = []
        candidates.sort()

        self.f(candidates, target, [], ans, 0)

        return ans