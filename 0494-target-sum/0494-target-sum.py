class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            next_dp = {}

            for total, count in dp.items():
                next_dp[total + num] = next_dp.get(total + num, 0) + count
                next_dp[total - num] = next_dp.get(total - num, 0) + count

            dp = next_dp

        return dp.get(target, 0)