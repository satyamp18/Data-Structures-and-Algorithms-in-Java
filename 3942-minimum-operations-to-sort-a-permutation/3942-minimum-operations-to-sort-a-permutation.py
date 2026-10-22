class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Find the index of 0
        idx0 = nums.index(0)

        # Check if nums is cyclically increasing:
        # nums[i] should be (nums[0] + i) % n for all i
        is_increasing = all(nums[i] == (nums[0] + i) % n for i in range(n))
        if is_increasing:
            if idx0 == 0:
                return 0
            # Rotate left directly vs. Rotate right using reverses
            return min(idx0, (n - idx0) + 2)

        # Check if nums is cyclically decreasing:
        # nums[i] should be (nums[0] - i) % n for all i
        is_decreasing = all(nums[i] == (nums[0] - i) % n for i in range(n))
        if is_decreasing:
            # Reverse first and rotate left vs. Rotate left first and reverse
            return min(n - idx0, idx0 + 2)

        # Neither cyclically increasing nor decreasing
        return -1