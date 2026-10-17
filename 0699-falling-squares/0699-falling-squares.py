class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        intervals = []
        ans = []
        max_height = 0

        for left, side in positions:
            right = left + side
            base = 0

            # Find the maximum height under the new square
            for l, r, h in intervals:
                if left < r and l < right:
                    base = max(base, h)

            height = base + side
            intervals.append((left, right, height))

            max_height = max(max_height, height)
            ans.append(max_height)

        return ans