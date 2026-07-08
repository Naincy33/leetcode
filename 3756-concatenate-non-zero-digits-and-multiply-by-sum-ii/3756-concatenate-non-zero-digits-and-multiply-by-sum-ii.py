class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7

        digits = []
        positions = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                positions.append(i)

        k = len(digits)

        # prefix number
        pref_num = [0] * (k + 1)

        # prefix digit sum
        pref_sum = [0] * (k + 1)

        # powers of 10
        power10 = [1] * (k + 1)

        for i in range(k):
            pref_num[i + 1] = (pref_num[i] * 10 + digits[i]) % MOD
            pref_sum[i + 1] = pref_sum[i] + digits[i]
            power10[i + 1] = (power10[i] * 10) % MOD

        import bisect

        ans = []

        for l, r in queries:
            # first non-zero position >= l
            left = bisect.bisect_left(positions, l)

            # first non-zero position > r
            right = bisect.bisect_right(positions, r)

            length = right - left

            if length == 0:
                ans.append(0)
                continue

            # Extract concatenated number
            x = (
                pref_num[right]
                - pref_num[left] * power10[length]
            ) % MOD

            digit_sum = pref_sum[right] - pref_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans