class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)

        prefix_num = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)
        prefix_count = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = int(ch)
            prefix_num[i + 1] = prefix_num[i]
            prefix_sum[i + 1] = prefix_sum[i]
            prefix_count[i + 1] = prefix_count[i]

            if d != 0:
                prefix_num[i + 1] = (
                    prefix_num[i] * 10 + d
                ) % MOD
                prefix_sum[i + 1] += d
                prefix_count[i + 1] += 1

        ans = []

        for l, r in queries:
            count = prefix_count[r + 1] - prefix_count[l]
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]

            if count == 0:
                ans.append(0)
                continue

            # Remove the non-zero digits before index l
            x = (
                prefix_num[r + 1]
                - prefix_num[l] * pow(10, count, MOD)
            ) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans