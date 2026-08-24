class Solution:

  def findShortestSubArray(self, nums: list[int]) -> int:
    first_seen = {}
    last_seen = {}
    counts = {}

    for i, num in enumerate(nums):
      if num not in first_seen:
        first_seen[num] = i
      last_seen[num] = i
      counts[num] = counts.get(num, 0) + 1

    degree = max(counts.values())
    min_length = len(nums)

    for num, count in counts.items():
      if count == degree:
        min_length = min(min_length, last_seen[num] - first_seen[num] + 1)

    return min_length