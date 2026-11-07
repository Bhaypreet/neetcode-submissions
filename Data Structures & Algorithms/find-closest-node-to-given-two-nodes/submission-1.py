class Solution:
    def f(self,node,adj,l):
        lis = [-1]*l
        ans = 1
        lis[node] = 0
        
        from collections import deque
        q = deque()
        q.append(node)
        while q :
            for _ in range(len(q)):
                u = q.popleft()
                for v in adj[u]:
                    if lis[v] == -1:
                        lis[v] = ans
                        q.append(v)
            ans+=1
        return lis

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        l = len(edges)
        adj = [[] for _ in range(len(edges))]
        for i in range (len(edges)):
            if edges[i] != -1 :
                adj[i].append(edges[i])
        
        dis1 = self.f(node1,adj,l)
        dis2 = self.f(node2,adj,l)

        minode = -1
        minidis = float('inf')

        for i in range(len(dis2)):
            if dis1[i] != -1 and dis2[i] != -1 :
                if max(dis1[i],dis2[i]) < minidis :
                    minidis = max(dis1[i],dis2[i])
                    minode = i

        return minode

        
