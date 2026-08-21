import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        def count_multiples(m: int) -> int:
            cnt = 0
            n = len(coins)
            for i in range(1, 1 << n):
                lcm_val = 1
                bits = 0
                for j in range(n):
                    if (i >> j) & 1:
                        bits += 1
                        lcm_val = math.lcm(lcm_val, coins[j])
                        if lcm_val > m:
                            break
                if lcm_val <= m:
                    if bits % 2 == 1:
                        cnt += m // lcm_val
                    else:
                        cnt -= m // lcm_val
            return cnt

        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % fc == 0 for fc in filtered_coins):
                filtered_coins.append(c)
        coins = filtered_coins

        left, right = 1, min(coins) * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_multiples(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans