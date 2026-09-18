class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        # Find the smallest valid interval starting from index l
        def get_interval(l):
            r = last[ord(s[l]) - ord('a')]
            i = l

            while i <= r:
                idx = ord(s[i]) - ord('a')

                # This character appeared before l,
                # so we cannot create a valid substring starting at l.
                if first[idx] < l:
                    return None

                r = max(r, last[idx])
                i += 1

            return (l, r)

        intervals = []

        # Only first occurrences can be the start of a minimal interval
        for i in range(n):
            idx = ord(s[i]) - ord('a')

            if i == first[idx]:
                interval = get_interval(i)

                if interval:
                    intervals.append(interval)

        # Greedily select intervals with earliest ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result