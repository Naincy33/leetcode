class Solution:
    def numDecodings(self, s):
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # one digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # two digits
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]

        return dp[n]
obj= Solution()
print(obj.numDecodings("2034126"))  # Output: 3