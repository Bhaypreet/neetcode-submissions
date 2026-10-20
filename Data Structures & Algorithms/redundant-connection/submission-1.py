class Solution:
    def f(self, node, target, adj, vis):
        if node == target:
            return True

        vis[node] = True

        for v in adj[node]:
            if not vis[v]:
                if self.f(v, target, adj, vis):
                    return True

        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            vis = [False] * (n + 1)

            # If v is already reachable from u, this edge creates a cycle
            if self.f(u, v, adj, vis):
                return [u, v]

            adj[u].append(v)
            adj[v].append(u)

        return []