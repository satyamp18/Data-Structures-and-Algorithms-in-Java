class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def backtrack(index, parts):
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                # Leading zeros are not allowed
                if len(part) > 1 and part[0] == '0':
                    continue

                # Each part must be between 0 and 255
                if int(part) > 255:
                    continue

                backtrack(index + length, parts + [part])

        backtrack(0, [])
        return result