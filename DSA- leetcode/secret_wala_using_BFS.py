from collections import defaultdict, deque

class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        meetings.sort(key=lambda x: x[2])

        secret = set([0, firstPerson])
        i = 0
        m = len(meetings)

        while i < m:
            time = meetings[i][2]
            graph = defaultdict(list)
            people = set()

            # build graph for SAME TIME only
            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1

            # BFS queue → ONLY people of this time who already know secret
            q = deque()
            visited = set()

            for p in people:
                if p in secret:
                    q.append(p)
                    visited.add(p)

            # BFS inside same-time graph
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        secret.add(v)
                        q.append(v)

        return list(secret)
obj = Solution()
print(obj.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))  # Output: [0,1,2,3,5]