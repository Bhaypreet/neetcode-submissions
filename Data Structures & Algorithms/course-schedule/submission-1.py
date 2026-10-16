class Solution:
    def f(self,node,adj,vis,path):
        vis[node] = True
        path[node] = True

        for v in adj[node]:
            if not vis[v]:
                if self.f(v,adj,vis,path) :
                    return True
            elif path[v]:
                return True
            
        path[node] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vis = [False for _ in range(numCourses)]

        path = [False for _ in range(numCourses)]

        adj = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            adj[b].append(a)

        for i in range(numCourses):
            if self.f(i,adj,vis,path):
                return False
        return True