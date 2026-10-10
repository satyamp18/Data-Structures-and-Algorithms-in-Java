class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        p_count = [0] * 26
        s_count = [0] * 26

        # Populate the pattern counts and the first window in s
        for i in range(m):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        result = []
        if s_count == p_count:
            result.append(0)

        # Slide the window across s
        for i in range(m, n):
            # Include the new character entering the window
            s_count[ord(s[i]) - ord('a')] += 1
            # Remove the character leaving the window
            s_count[ord(s[i - m]) - ord('a')] -= 1

            if s_count == p_count:
                result.append(i - m + 1)

        return result