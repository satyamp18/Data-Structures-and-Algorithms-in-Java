
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # cost[l][r] = minimum changes to make s[l:r+1]
        # a semi-palindrome
        cost = [[INF] * n for _ in range(n)]

        # Precompute semi-palindrome costs
        for l in range(n):
            for r in range(l + 1, n):
                length = r - l + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    groups = length // d

                    for offset in range(d):
                        left = l + offset
                        right = l + offset + (groups - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[l][r] = min(cost[l][r], changes)

        # dp[p][i] = minimum cost to divide first i characters
        # into exactly p semi-palindromic substrings
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
