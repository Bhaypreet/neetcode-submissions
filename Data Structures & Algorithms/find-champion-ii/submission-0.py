class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[v].append(u)
        ans = 0
        maxi = -1
        i = 0
        for item in adj:
            if len(item) == 0:
                ans+=1
                maxi = i
            if ans > 1:
                return -1
            i+=1

        return maxi
            