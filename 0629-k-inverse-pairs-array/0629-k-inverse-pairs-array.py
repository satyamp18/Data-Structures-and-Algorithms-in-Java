class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[j] = number of arrays with exactly j inverse pairs
        dp = [0] * (k + 1)
        dp[0] = 1

        for num in range(1, n + 1):
            new_dp = [0] * (k + 1)

            window = 0

            for j in range(k + 1):
                window += dp[j]

                # The new number can create at most num-1
                # new inverse pairs.
                if j >= num:
                    window -= dp[j - num]

                window %= MOD
                new_dp[j] = window

            dp = new_dp

        return dp[k]