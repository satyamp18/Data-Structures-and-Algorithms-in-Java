class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        left_q = 0
        right_q = 0
        diff = 0

        # First half
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                diff += int(num[i])

        # Second half
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                diff -= int(num[i])

        # Odd number of '?' means Alice can always force a win
        if (left_q + right_q) % 2 == 1:
            return True

        # Bob can win only if the fixed-digit difference
        # can exactly compensate for the '?' difference.
        return diff != 9 * (right_q - left_q) // 2