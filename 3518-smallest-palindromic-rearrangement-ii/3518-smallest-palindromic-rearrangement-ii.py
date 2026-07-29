from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""

        for ch, cnt in freq.items():
            if cnt % 2:
                mid = ch
            half[ord(ch) - ord('a')] = cnt // 2

        # Compute multinomial:
        # total! / (c1! * c2! * ...)
        def comb(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) // i
            return res

        rem = sum(half)
        ways = 1
        used = 0
        for c in half:
            if c:
                ways *= comb(used + c, c)
                used += c

        if ways < k:
            return ""

        ans = []
        rem = sum(half)

        while rem:
            for i in range(26):
                if half[i] == 0:
                    continue

                # Ways if we place this character
                nxt = ways * half[i] // rem

                if nxt >= k:
                    ans.append(chr(i + ord('a')))
                    half[i] -= 1
                    ways = nxt
                    rem -= 1
                    break
                else:
                    k -= nxt

        left = "".join(ans)
        return left + mid + left[::-1]