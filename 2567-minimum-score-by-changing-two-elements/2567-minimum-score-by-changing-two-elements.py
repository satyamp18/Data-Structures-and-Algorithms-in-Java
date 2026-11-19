from typing import List


class Solution:

  def minimizeSum(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 3:
      return 0

    nums.sort()

    # Since we can set two elements to the exact same value (for instance, matching an existing element),
    # the minimum absolute difference (low score) can always be made 0.
    # Thus, the total score equals the maximum absolute difference (high score),
    # which is (remaining max - remaining min) after dropping two elements.
    return min(
        nums[-1] - nums[2],  # Drop the 2 smallest elements
        nums[-3] - nums[0],  # Drop the 2 largest elements
        nums[-2] - nums[1],  # Drop 1 smallest and 1 largest element
    )