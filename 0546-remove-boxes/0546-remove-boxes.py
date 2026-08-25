from functools import cache


class Solution:

  def removeBoxes(self, boxes: list[int]) -> int:
    @cache
    def dp(l: int, r: int, k: int) -> int:
      if l > r:
        return 0

      # Merge contiguous duplicate elements at the start to reduce redundant states
      while l + 1 <= r and boxes[l] == boxes[l + 1]:
        l += 1
        k += 1

      # Option 1: Remove boxes[l] along with the k identical boxes attached to its left
      res = (k + 1) * (k + 1) + dp(l + 1, r, 0)

      # Option 2: Remove a middle segment boxes[l+1...m-1] to group boxes[l] with boxes[m]
      for m in range(l + 1, r + 1):
        if boxes[m] == boxes[l]:
          res = max(res, dp(l + 1, m - 1, 0) + dp(m, r, k + 1))

      return res

    return dp(0, len(boxes) - 1, 0)