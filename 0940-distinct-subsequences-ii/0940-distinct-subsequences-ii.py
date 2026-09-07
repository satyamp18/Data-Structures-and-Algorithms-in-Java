class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp = number of distinct subsequences including empty subsequence
        dp = 1

        # last[ch] = dp value before the previous occurrence of ch
        last = {}

        for ch in s:
            new_dp = (2 * dp) % MOD

            if ch in last:
                new_dp = (new_dp - last[ch]) % MOD

            last[ch] = dp
            dp = new_dp

        # Remove the empty subsequence
        return (dp - 1) % MOD