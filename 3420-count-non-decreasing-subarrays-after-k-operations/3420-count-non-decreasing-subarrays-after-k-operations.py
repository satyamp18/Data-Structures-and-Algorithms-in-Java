
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dq = deque()

        right = n - 1
        cost = 0
        ans = 0

        for left in range(n - 1, -1, -1):
            # Merge smaller values into the current value
            while dq and nums[dq[-1]] < nums[left]:
                idx = dq.pop()
                next_idx = dq[-1] if dq else right + 1

                cost += (next_idx - idx) * (nums[left] - nums[idx])

            dq.append(left)

            # Reduce the window while its cost exceeds k
            while cost > k:
                cost -= nums[dq[0]] - nums[right]

                if dq[0] == right:
                    dq.popleft()

                right -= 1

            # Count all valid subarrays starting at left
            ans += right - left + 1

        return ans
