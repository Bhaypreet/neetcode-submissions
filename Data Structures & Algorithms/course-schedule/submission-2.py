class Solution:
    def f(self,adj,i,vis,path):
        vis[i] = True
        path[i] = True

        for v in adj[i]:
            if vis[v] is False:
                if self.f(adj,v,vis,path):
                    return True
            elif path[v] is True:
                return True

        path[i] = False
            
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)

        path = [False for _ in range(numCourses)]
        vis = [False for _ in range(numCourses)]
        
        for i in range(numCourses):
            if vis[i] is False:
                if self.f(adj,i,vis,path):
                    return False
        return True