class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]

        for a,b in trust:
            adj[b].append(a)

        for i in range(n+1):
            if len(adj[i]) == n-1 :
                if all(a != i for a, b in trust):
                    return i

        return -1