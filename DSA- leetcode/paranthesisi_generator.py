class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(open, close, curr):
            if open == 0 and close == 0:
                result.append(curr)
                return

            # add '(' if available
            if open > 0:
                backtrack(open - 1, close, curr + '(')

            # add ')' only if valid
            if close > open:
                backtrack(open, close - 1, curr + ')')

        backtrack(n, n, "")
        return result
obj = Solution()
print(obj.generateParenthesis(4))