class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))

        last = [-1] * 10

        # Store last occurrence of every digit
        for i, d in enumerate(s):
            last[int(d)] = i

        # Find first digit that can be improved
        for i, d in enumerate(s):
            for x in range(9, int(d), -1):

                if last[x] > i:
                    s[i], s[last[x]] = s[last[x]], s[i]
                    return int("".join(s))

        return num