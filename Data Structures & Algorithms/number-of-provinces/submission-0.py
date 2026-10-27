class Solution:
    def f(self,grid,i,adj,vis):
        vis[i] = True
        a = 0
        for v in adj[i]:
            if not vis[v]:
                self.f(grid,v,adj,vis)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = [[] for _ in range(len(isConnected))]
        vis = [False]*len(isConnected)
        ans = 0

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    if i != j :
                        adj[i].append(j)
                        adj[j].append(i)
        for i in range(len(isConnected)):
            if vis[i] is False:
                ans+=1
                self.f(isConnected,i,adj,vis)
        return ans
