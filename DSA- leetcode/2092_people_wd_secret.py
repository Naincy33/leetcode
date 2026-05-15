class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        meetings.sort(key=lambda x: x[2])

        parent = [i for i in range(n)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pb] = pa

        # initial secret sharing
        union(0, firstPerson)

        i = 0
        m = len(meetings)

        while i < m:
            time = meetings[i][2]
            participants = []

            # union same-time meetings
            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                participants.append(x)
                participants.append(y)
                i += 1

            root0 = find(0)

            # propagate secret
            for p in participants:
                if find(p) == root0:
                    parent[p] = root0

            # reset others
            for p in participants:
                if find(p) != root0:
                    parent[p] = p

        # collect answer
        ans = []
        root0 = find(0)
        for i in range(n):
            if find(i) == root0:
                ans.append(i)

        return ans
obj = Solution()
print(obj.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))  # Output: [0,1,2,3,5]