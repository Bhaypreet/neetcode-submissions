class Solution:
    def f(self,adj,parent,vis,node):
        from collections import deque
        vis[node] = True
        q = deque()
        q.append(node)
        while(q):
            u = q.popleft()
            for v in adj[u]:
                if vis[v] is False:
                    parent[v] = u
                    vis[v] = True
                    q.append(v)
                elif parent[u] != v :
                    return True
        return False


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        ans = 0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis= [False]*n
        parent = [-1]*n

        for i in range(n):
            if vis[i] is False:
                ans+=1
                if self.f(adj,parent,vis,i):
                    return False
        if ans>1 :
            return False
        return True