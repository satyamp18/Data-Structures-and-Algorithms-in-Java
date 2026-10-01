from bisect import bisect_left

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int,
                             queries: list[list[int]]) -> list[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        vals = [nums[i] for i in order]

        pos = [0] * n
        for i, node in enumerate(order):
            pos[node] = i

        # Build connected components and identify gaps
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[order[i]] = cid

        # Greedily jump as far as possible within maxDiff
        nxt = list(range(n))
        j = 0
        for i in range(n):
            j = max(j, i)
            while j + 1 < n and vals[j + 1] - vals[i] <= maxDiff:
                j += 1
            nxt[i] = j

        # Binary lifting over jumps
        LOG = max(1, n.bit_length())
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            if comp[u] != comp[v]:
                ans.append(-1)
                continue

            l, r = sorted((pos[u], pos[v]))
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][l] < r:
                    l = up[k][l]
                    steps += 1 << k

            ans.append(steps + 1)

        return ans