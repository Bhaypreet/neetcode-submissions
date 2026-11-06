class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[v].append(u)
        ans = 0
        a = -1
        for i in range(n):
            if len(adj[i]) == 0:
                ans+=1
                a = i
        if ans >1 :
            return -1
        return a