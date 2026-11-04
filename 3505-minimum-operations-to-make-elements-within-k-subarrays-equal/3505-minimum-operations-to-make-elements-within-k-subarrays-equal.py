class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        MOD_INF = float('inf')

        # Coordinate compression
        values = sorted(set(nums))
        size = len(values)
        pos = {v: i for i, v in enumerate(values)}

        # Fenwick Tree for frequency and sum
        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.cnt = [0] * (n + 1)
                self.sums = [0] * (n + 1)

            def update(self, i, count, total):
                i += 1
                while i <= self.n:
                    self.cnt[i] += count
                    self.sums[i] += total
                    i += i & -i

            def query(self, i):
                count = total = 0
                while i > 0:
                    count += self.cnt[i]
                    total += self.sums[i]
                    i -= i & -i
                return count, total

            def kth(self, k):
                idx = 0
                bit = 1 << (self.n.bit_length() - 1)

                while bit:
                    nxt = idx + bit

                    if nxt <= self.n and self.cnt[nxt] < k:
                        idx = nxt
                        k -= self.cnt[nxt]

                    bit >>= 1

                return idx

        bit = Fenwick(size)
        window_sum = 0

        # Initialize first window
        for i in range(x):
            bit.update(pos[nums[i]], 1, nums[i])
            window_sum += nums[i]

        costs = []

        def get_cost():
            median_idx = bit.kth((x + 1) // 2)
            median = values[median_idx]

            left_count, left_sum = bit.query(median_idx + 1)

            right_count = x - left_count
            right_sum = window_sum - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        costs.append(get_cost())

        # Calculate cost of every sliding window
        for i in range(x, n):
            old = nums[i - x]
            new = nums[i]

            bit.update(pos[old], -1, -old)
            bit.update(pos[new], 1, new)

            window_sum += new - old

            costs.append(get_cost())

        # DP for selecting k non-overlapping windows
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [MOD_INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Select window ending at i-1
                if i >= x:
                    start = i - x

                    curr[i] = min(
                        curr[i],
                        prev[start] + costs[start]
                    )

            prev = curr

        return prev[n]