class Solution:
    def f(self,adj,node,vis):
        from collections import deque
        q = deque()
        vis[node] = True
        q.append(node)

        while(q):
            u = q.popleft()
            for v in adj[u]:
                if not vis[v]:
                    q.append(v)
                    vis[v] = True


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u ,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False for _ in range(n)]
        
        ans = 0

        for i in range(n):
            if vis[i] is False:
                ans+=1
                self.f(adj,i,vis)
        return ans
        