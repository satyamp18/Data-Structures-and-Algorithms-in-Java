from math import gcd
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_val = max(nums)
        freq = [0] * (max_val + 1)

        for num in nums:
            freq[num] += 1

        # Count pairs whose GCD is exactly g
        gcd_count = [0] * (max_val + 1)

        for g in range(max_val, 0, -1):
            count = 0

            # Count numbers divisible by g
            for multiple in range(g, max_val + 1, g):
                count += freq[multiple]

            # All pairs among these numbers have GCD divisible by g
            pairs = count * (count - 1) // 2

            # Remove pairs whose GCD is a larger multiple of g
            for multiple in range(2 * g, max_val + 1, g):
                pairs -= gcd_count[multiple]

            gcd_count[g] = pairs

        # Prefix sums: cumulative number of pairs with GCD <= g
        prefix = []
        total = 0

        for g in range(1, max_val + 1):
            total += gcd_count[g]
            prefix.append(total)

        # Find the GCD value at each zero-based query index
        answer = []
        for q in queries:
            answer.append(bisect_left(prefix, q + 1) + 1)

        return answer