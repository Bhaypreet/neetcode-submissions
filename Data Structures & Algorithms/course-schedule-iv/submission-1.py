class Solution:
    def f(self,a,b,adj):
        
        from collections import deque
        q = deque()
        q.append(b)
        visited = {a}


        while(q):
            node = q.popleft()
            for v in adj[node]:
                if v == a:
                    return True
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return False


    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj[b].append(a)

        lis = []

        for u,v in queries:
            lis.append(self.f(u,v,adj))

        return lis
        