class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        memo = {}

        def dp(i, M):
            # All piles taken
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            for X in range(1, 2 * M + 1):
                # Stones current player takes
                taken = suffix[i] - suffix[i + X]

                # Opponent's maximum stones
                opponent = dp(i + X, max(M, X))

                # Current player's total
                current = taken + (suffix[i + X] - opponent)

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)