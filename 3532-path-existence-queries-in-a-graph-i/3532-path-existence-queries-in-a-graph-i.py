from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        # comp[i] = connected component id of node i
        comp = [0] * n

        component_id = 0

        for i in range(1, n):
            # If consecutive nodes cannot connect,
            # a new connected component starts
            if nums[i] - nums[i - 1] > maxDiff:
                component_id += 1

            comp[i] = component_id

        answer = []

        for u, v in queries:
            answer.append(comp[u] == comp[v])

        return answer