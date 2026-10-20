class Solution:
    def f(self,vis,node,adj):
        vis[node] = True
        from collections import deque
        q = deque()
        height = 0
        q.append(node)

        while(q):
            height+=1
            for i in range(len(q)):
                u = q.popleft()

                for v in adj[u]:
                    if not vis[v]:
                        vis[v] = True
                        q.append(v)
        
        return height

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        mini = 0 
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lis = []

        for i in range(n):
            vis = [False]*n
            a = self.f(vis,i,adj)
            if len(lis) == 0:
                lis.append(i)
                mini = a
            elif a == mini:
                lis.append(i)
            elif a < mini :
                mini = a
                lis = [i]

        return lis










        