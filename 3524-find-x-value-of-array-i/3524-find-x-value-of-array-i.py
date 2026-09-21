class Solution:
    def resultArray(self, nums, k):
        # dp[r] = number of subarrays ending at previous index
        # whose product % k == r
        dp = [0] * k

        # answer[r] = total number of subarrays
        # whose product % k == r
        answer = [0] * k

        for num in nums:
            x = num % k

            new_dp = [0] * k

            # Start a new subarray with only nums[i]
            new_dp[x] += 1

            # Extend all previous subarrays
            for r in range(k):
                new_r = (r * x) % k
                new_dp[new_r] += dp[r]

            # Add current subarrays to the answer
            for r in range(k):
                answer[r] += new_dp[r]

            dp = new_dp

        return answer