class Solution:
    def f(self,node,adj,parent,vis):
        from collections import deque
        q = deque()
        vis[node] = True
        q.append(node)

        while(q):
            u = q.popleft()
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
                    parent[v] = u
                elif parent[u] != v:
                    return True
        return False




    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [-1]*n
        # for u,v in edges:
        #     parent[v].append(u)

        vis = [False for _ in range(n)]

        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)
        ans = 0
        for i in range(n):
            if vis[i] is False:
                ans += 1
                if self.f(i,adj,parent,vis):
                    return False
        if ans > 1:
            return False
        return True

