class Solution:
    def f(self,node,adj,vis,path,lis):
        vis[node] = True
        path[node] = True

        for v in adj[node]:
            if vis[v] is False:
                if self.f(v,adj,vis,path,lis):
                    return True

            elif path[v] :
                return True
        lis.append(node)
        path[node] = False
        
        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        vis = [False for _ in range(numCourses)]
        path = [False for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            adj[b].append(a)

        lis = []
        lis2 = []

        for i in range(numCourses):
            if  self.f(i,adj,vis,path,lis):
                return []
        return lis[::-1]