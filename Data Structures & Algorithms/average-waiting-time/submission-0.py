class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        ans = 0
        ttf = 0

        for u,v in customers:
            if u >= ttf :
                ans+=v
                ttf= u+v
            else:
                ans+=v+ttf-u
                ttf+=v

        return ans/n
