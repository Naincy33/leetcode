class Solution:
    def stoneGameIX(self, stones):
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        c0, c1, c2 = cnt

        # Only one of remainder 1 or 2 exists
        if min(c1, c2) == 0:
            return max(c1, c2) > 2 and c0 % 2 == 1

        # Both 1 and 2 exist
        return abs(c1 - c2) > 2 or c0 % 2 == 0