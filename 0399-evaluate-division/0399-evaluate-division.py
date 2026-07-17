from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):

        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(src, dst, visited):

            if src not in graph:
                return -1

            if src == dst:
                return 1

            visited.add(src)

            for nei, weight in graph[src]:

                if nei not in visited:

                    ans = dfs(nei, dst, visited)

                    if ans != -1:
                        return weight * ans

            return -1

        ans = []

        for src, dst in queries:
            ans.append(dfs(src, dst, set()))

        return ans