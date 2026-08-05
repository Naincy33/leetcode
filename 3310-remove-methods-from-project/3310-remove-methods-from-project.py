from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build graph
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods using DFS
        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True
            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        # Check if any non-suspicious method invokes a suspicious one
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return remaining methods
        return [i for i in range(n) if not suspicious[i]]