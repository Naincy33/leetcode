class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Last occurrence of each character
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        visited = set()

        for i, ch in enumerate(s):
            # Skip if already in answer
            if ch in visited:
                continue

            # Remove bigger characters if they occur later
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)