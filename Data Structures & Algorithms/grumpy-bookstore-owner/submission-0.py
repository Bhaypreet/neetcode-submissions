class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        maxi = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                ans+=customers[i]

        l = 0
        r = minutes-1
        while(r < len(customers)):
            a = ans
            for i in range(l,r+1):
                if grumpy[i] == 1:
                    a+=customers[i]
            maxi = max(maxi,a)
            l+=1
            r+=1

        return maxi