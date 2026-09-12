from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Add original index
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((r, l, w, i))

        # Sort by ending position
        arr.sort()

        ends = [x[0] for x in arr]

        # prev[i] = last interval that ends before arr[i] starts
        prev = [0] * n

        for i in range(n):
            start = arr[i][1]

            # Need end < start because boundaries are overlapping
            prev[i] = bisect_left(ends, start, 0, i) - 1

        # dp[k][i] = best result using first i intervals
        # We store (score, tuple of indices)
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        def better(a, b):
            # Higher score is better
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # Same score -> lexicographically smaller indices
            return a if a[1] < b[1] else b

        for k in range(1, 5):
            for i in range(1, n + 1):
                # Don't take current interval
                best = dp[k][i - 1]

                # Take current interval
                end, start, weight, idx = arr[i - 1]

                p = prev[i - 1] + 1

                old_score, old_indices = dp[k - 1][p]

                new_indices = tuple(sorted(old_indices + (idx,)))
                candidate = (
                    old_score + weight,
                    new_indices
                )

                best = better(best, candidate)
                dp[k][i] = best

        return list(dp[4][n][1])