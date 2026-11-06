class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda a: a[1])

        sorted_queries = sorted(
            [(q, i) for i, q in enumerate(queries)]
        )

        freq = {}
        left = right = 0
        result = [0] * len(queries)

        for q, idx in sorted_queries:
            start = q - x
            end = q

            # Add logs within the right boundary
            while right < len(logs) and logs[right][1] <= end:
                server = logs[right][0]
                freq[server] = freq.get(server, 0) + 1
                right += 1

            # Remove logs outside the left boundary
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]

                left += 1

            result[idx] = n - len(freq)

        return result