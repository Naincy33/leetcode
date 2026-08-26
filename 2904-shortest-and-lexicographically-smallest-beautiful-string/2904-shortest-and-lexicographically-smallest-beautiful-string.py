class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # We have exactly k ones
            if ones == k:
                # Move left while keeping exactly k ones
                while left <= right and s[left] == '0':
                    left += 1

                # Remove unnecessary zeros after the first 1
                start = left

                # Find the earliest possible start while keeping k ones
                while start <= right and s[start] == '1':
                    if start + 1 <= right and s[start + 1] == '0':
                        break
                    start += 1

                # The shortest substring ending at right
                candidate = s[left:right + 1]

                if not ans or len(candidate) < len(ans):
                    ans = candidate
                elif len(candidate) == len(ans):
                    ans = min(ans, candidate)

                # Move left past the first 1
                ones -= 1
                left += 1

        return ans