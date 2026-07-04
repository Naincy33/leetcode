class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]

        # Create adjacency list
        for u, v, dist in roads:
            adj[u].append((v, dist))
            adj[v].append((u, dist))

        visited = [False] * (n + 1)
        ans = float('inf')

        def dfs(node):
            nonlocal ans

            visited[node] = True

            for neighbour, dist in adj[node]:
                # Update minimum edge weight
                ans = min(ans, dist)

                if not visited[neighbour]:
                    dfs(neighbour)

        dfs(1)

        return ans