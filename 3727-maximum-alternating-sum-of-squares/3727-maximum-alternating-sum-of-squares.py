class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted((x * x for x in nums), reverse=True)
        n = len(squares)
        positives = (n + 1) // 2

        return sum(squares[:positives]) - sum(squares[positives:])