class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j] = number of ways to draw exactly j segments
        # using points 0...i
        dp = [[0] * (k + 1) for _ in range(n)]

        # With 0 segments, there is always exactly 1 way:
        # choose nothing.
        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(1, n):
                # Add ways where previous segments end at or before i-1
                prefix = (prefix + dp[i - 1][j - 1]) % MOD

                # Option 1: Don't end a segment at i
                # Option 2: Add segment [a, i]
                dp[i][j] = (dp[i - 1][j] + prefix) % MOD

        return dp[n - 1][k]