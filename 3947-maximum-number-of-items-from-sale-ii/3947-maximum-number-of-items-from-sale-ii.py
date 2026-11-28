from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        max_f = max(n, max((f for f, _ in items), default=0))

        # Count occurrences of each factor
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        # mult_count[d] = total items with factor a multiple of d
        mult_count = [0] * (max_f + 1)
        for d in range(1, max_f + 1):
            if freq[d] == 0:
                continue
            for m in range(d, max_f + 1, d):
                mult_count[d] += freq[m]

        min_price = min(p for _, p in items)

        # Each eligible item i provides `gain` boosted units (1 bought + 1 free = 2 copies)
        # at cost `p` per unit. Only include if p / 2 < min_price (p < 2 * min_price).
        boosted_batches = []
        for f, p in items:
            gain = mult_count[f] - 1
            if gain > 0 and p < 2 * min_price:
                boosted_batches.append((p, gain))

        boosted_batches.sort(key=lambda x: x[0])

        total_copies = 0
        rem_budget = budget

        for p, cnt in boosted_batches:
            if rem_budget < p:
                break
            take = min(cnt, rem_budget // p)
            total_copies += take * 2
            rem_budget -= take * p

        # Spend remaining budget on the cheapest item (1 copy per purchase)
        total_copies += rem_budget // min_price
        return total_copies