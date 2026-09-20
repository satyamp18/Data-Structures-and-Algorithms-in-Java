class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s):
            # a -> 26, b -> 25, ..., z -> 1
            reverse_value = 26 - (ord(ch) - ord('a'))

            # i is 0-based, so position = i + 1
            ans += reverse_value * (i + 1)

        return ans