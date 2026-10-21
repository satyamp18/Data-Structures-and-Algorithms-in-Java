
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Case 1: Already sorted
        if s == ''.join(sorted(s)):
            return 0

        # Case 2: Length 2 cannot be sorted
        # because sorting the entire string is forbidden
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Case 3: One operation is enough
        if s[0] == mn or s[-1] == mx:
            return 1

        # Case 4: Minimum or maximum is inside the string
        if mn in s[1:-1] or mx in s[1:-1]:
            return 2

        # Case 5: Need three operations
        return 3
