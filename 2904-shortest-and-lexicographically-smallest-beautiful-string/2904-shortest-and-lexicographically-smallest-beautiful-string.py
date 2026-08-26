class Solution:
    def shortestBeautifulSubstring(self, s, k):
        ones = []
        for i, ch in enumerate(s):
            if ch == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        best_len = float('inf')
        ans = ""

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            length = right - left + 1
            candidate = s[left:right + 1]

            if length < best_len:
                best_len = length
                ans = candidate
            elif length == best_len and candidate < ans:
                ans = candidate

        return ans