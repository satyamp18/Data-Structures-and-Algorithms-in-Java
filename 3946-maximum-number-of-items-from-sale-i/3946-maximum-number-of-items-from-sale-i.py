from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n

        # Count how many other items j != i have factor_j divisible by factor_i
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            bonus[i] = cnt

        # dp[b] = max total item copies obtainable with budget b
        dp = [0] * (budget + 1)

        for factor, price in items:
            if price > budget:
                continue

            idx = items.index([factor, price]) if False else 0  # replaced below
            break

        # Re-write cleanly using enumerate so duplicate [factor, price] items keep distinct indices
        dp = [0] * (budget + 1)
        for i, (_, price) in enumerate(items):
            if price > budget:
                continue

            # 1) First copy of item i: yields 1 + bonus[i] copies (0/1 transition)
            gain_first = 1 + bonus[i]
            for b in range(budget, price - 1, -1):
                if dp[b - price] + gain_first > dp[b]:
                    dp[b] = dp[b - price] + gain_first

            # 2) Additional copies of item i: yields 1 copy each (unbounded transition)
            for b in range(price, budget + 1):
                if dp[b - price] + 1 > dp[b]:
                    dp[b] = dp[b - price] + 1

        return max(dp)