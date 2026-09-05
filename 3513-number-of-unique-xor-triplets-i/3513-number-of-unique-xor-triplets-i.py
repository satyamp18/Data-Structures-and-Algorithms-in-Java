class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        # Find smallest power of 2 greater than n
        p = 1
        while p <= n:
            p <<= 1

        return p