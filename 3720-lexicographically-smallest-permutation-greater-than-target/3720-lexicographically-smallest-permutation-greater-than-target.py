class Solution:
    def lexGreaterPermutation(self, s, target):
        from collections import Counter

        count = Counter(s)
        n = len(s)

        def build(pos, greater):
            if pos == n:
                return "" if greater else None

            if greater:
                for ch in sorted(count):
                    if count[ch]:
                        count[ch] -= 1
                        res = build(pos + 1, True)
                        count[ch] += 1
                        if res is not None:
                            return ch + res
                return None

            for ch in sorted(count):
                if not count[ch]:
                    continue

                if ch < target[pos]:
                    continue

                count[ch] -= 1

                if ch > target[pos]:
                    res = build(pos + 1, True)
                else:
                    res = build(pos + 1, False)

                count[ch] += 1

                if res is not None:
                    return ch + res

            return None

        return build(0, False) or ""