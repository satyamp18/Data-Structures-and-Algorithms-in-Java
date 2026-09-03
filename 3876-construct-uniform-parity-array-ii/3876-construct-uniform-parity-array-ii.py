class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')

        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)

        # If all numbers are already even
        if min_odd == float('inf'):
            return True

        # To make all numbers odd, every even number
        # must be able to subtract a smaller odd number.
        for x in nums1:
            if x % 2 == 0 and min_odd >= x:
                return False

        return True