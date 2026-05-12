from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = defaultdict(list)
        indegree = [0] * numCourses

        # build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # nodes with indegree 0
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:

            node = q.popleft()
            completed += 1

            for nei in graph[node]:

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return completed == numCourses
# Example usage:
solution = Solution()       
numCourses = 2
prerequisites = [[1, 1]]
print(solution.canFinish(numCourses, prerequisites))  