class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[i][j] = maximum score for stoneValue[i...j]
        dp = [[0] * n for _ in range(n)]

        # left_best[i][j] =
        # max(sum(i...k) + dp[i][k]) for k <= j
        left_best = [[0] * n for _ in range(n)]

        # right_best[i][j] =
        # max(sum(k...j) + dp[k][j]) for k >= i
        right_best = [[0] * n for _ in range(n)]

        # Base case
        for i in range(n):
            left_best[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                # Build right_best[i][j]
                right_value = (
                    prefix[j + 1] - prefix[i + 1]
                    + dp[i + 1][j]
                )

                if i + 1 < j:
                    right_best[i][j] = max(
                        right_best[i + 1][j],
                        right_value
                    )
                else:
                    right_best[i][j] = right_value

                # Binary search for split point
                lo = i
                hi = j

                while lo < hi:
                    mid = (lo + hi) // 2

                    left_sum = prefix[mid + 1] - prefix[i]

                    if 2 * left_sum >= total:
                        hi = mid
                    else:
                        lo = mid + 1

                k = lo

                # No right part with left >= right
                if k == j:
                    dp[i][j] = left_best[i][j - 1]

                else:
                    left_sum = prefix[k + 1] - prefix[i]
                    right_sum = total - left_sum

                    if left_sum == right_sum:
                        # Alice can choose either side
                        dp[i][j] = max(
                            left_best[i][k],
                            right_best[k][j]
                        )

                    else:
                        # Largest split where left < right
                        if k > i:
                            dp[i][j] = max(
                                dp[i][j],
                                left_best[i][k - 1]
                            )

                        # Splits where left > right
                        dp[i][j] = max(
                            dp[i][j],
                            right_best[k][j]
                        )

                # Update left_best
                current = total + dp[i][j]

                left_best[i][j] = max(
                    left_best[i][j - 1],
                    current
                )

        return dp[0][n - 1]