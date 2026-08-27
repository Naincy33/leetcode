from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        n = len(s)

        # right se position choose karenge jahan
        # target[i] se strictly bada character laga sakein
        for i in range(n - 1, -1, -1):

            # target[0:i] ko exactly same rakhne ke liye
            # characters consume karo
            prefix_ok = True
            used = Counter()

            for j in range(i):
                if cnt[target[j]] - used[target[j]] <= 0:
                    prefix_ok = False
                    break
                used[target[j]] += 1

            if not prefix_ok:
                continue

            # Position i par target[i] se bada smallest character
            for ch in sorted(cnt):
                if ch > target[i] and cnt[ch] - used[ch] > 0:

                    ans = target[:i] + ch

                    # Remaining characters
                    remaining = cnt.copy()
                    for c, freq in used.items():
                        remaining[c] -= freq

                    remaining[ch] -= 1

                    # Baaki sab smallest order mein
                    for c in sorted(remaining):
                        ans += c * remaining[c]

                    return ans

        return ""