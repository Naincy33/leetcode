from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        
        n = len(edges) + 1
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS to find max depth
        visited = [False] * (n + 1)
        queue = deque([(1, 0)])  # (node, depth)
        visited[1] = True
        
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    queue.append((nei, depth + 1))
        
        # Answer = 2^(k-1)
        return pow(2, max_depth - 1, MOD) if max_depth > 0 else 1
# Time complexity: O(n) for BFS traversal
# Space complexity: O(n) for the graph and visited array
solution = Solution()               
edges = [[1, 2], [1, 3], [2, 4], [2, 5]]
print(solution.assignEdgeWeights(edges))    
edges = [[1, 2], [1, 3], [2, 4], [3, 5]]
print(solution.assignEdgeWeights(edges))