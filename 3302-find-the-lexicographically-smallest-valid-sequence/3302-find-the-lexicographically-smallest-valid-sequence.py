class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:

        n = len(word1)
        m = len(word2)

        # last[j] = latest index in word1 where
        # word2[j] can be matched while keeping
        # the remaining suffix possible.
        last = [-1] * m

        i = n - 1
        j = m - 1

        # Build last[] from right to left
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1

            i -= 1

        ans = []

        # We are allowed to use at most one mismatch
        canSkip = True

        j = 0

        # Greedily choose the earliest possible indices
        for i in range(n):

            if j == m:
                break

            # Case 1: Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2: Use our one allowed mismatch
            elif canSkip and (
                j == m - 1 or i < last[j + 1]
            ):
                ans.append(i)
                j += 1
                canSkip = False

        # Did we select all characters?
        return ans if j == m else []