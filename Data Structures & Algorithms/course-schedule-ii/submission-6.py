class Solution:
    def f(self,adj,node,vis,path,lis):
        vis[node] = True
        path[node] = True

        for v in adj[node]:
            if vis[v] is False:
                
                if self.f(adj,v,vis,path,lis):
                    return True

            elif path[v] :
                return True
        lis.append(node)
        path[node] = False
        return False
        

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)

        path = [False]*numCourses
        vis = [False]*numCourses
        lis = []

        for i in range(numCourses):
            # if vis[i] is False:
            if self.f(adj,i,vis,path,lis):
                return []

        return lis[::-1]


        