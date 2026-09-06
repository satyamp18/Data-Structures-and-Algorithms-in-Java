class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[j] = number of ways to form t[:j] using processed chars of s
        dp = [0] * (n + 1)
        dp[0] = 1

        for char in s:
            # Traverse backwards so old values aren't overwritten
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]