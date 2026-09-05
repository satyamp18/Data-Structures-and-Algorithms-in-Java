from bisect import bisect_left, bisect_right

class SegmentTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [-1] * (4 * size)

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.tree[node] = max(self.tree[node], val)
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if r < start or end < l:
            return -1
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones_in_s = s.count('1')

        # Decompose s into alternating blocks of '0's and '1's
        blocks = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks.append((s[i], i, j - 1))
            i = j

        # Identify every '1'-block surrounded by '0'-blocks
        candidates = []
        for k in range(1, len(blocks) - 1):
            if blocks[k][0] == '1':
                z_left = blocks[k - 1]
                z_right = blocks[k + 1]
                candidates.append({
                    'z_left_start': z_left[1],
                    'z_left_end': z_left[2],
                    'z_right_start': z_right[1],
                    'z_right_end': z_right[2],
                })

        num_queries = len(queries)
        ans = [0] * num_queries

        cand_gains = [
            (c['z_left_end'] - c['z_left_start'] + 1) + (c['z_right_end'] - c['z_right_start'] + 1)
            for c in candidates
        ]

        # Map candidate events by z_left_start descending
        cand_by_left = [[] for _ in range(n + 1)]
        for idx, c in enumerate(candidates):
            cand_by_left[c['z_left_start']].append(idx)

        # Queries grouped by L
        queries_by_l = [[] for _ in range(n + 1)]
        for q_idx, (l, r) in enumerate(queries):
            queries_by_l[l].append((r, q_idx))

        seg_tree = SegmentTree(n + 1)
        max_full_gain = [0] * num_queries

        for l in range(n - 1, -1, -1):
            for c_idx in cand_by_left[l]:
                r_end = candidates[c_idx]['z_right_end']
                gain = cand_gains[c_idx]
                seg_tree.update(1, 0, n, r_end, gain)

            for r, q_idx in queries_by_l[l]:
                res = seg_tree.query(1, 0, n, 0, r)
                if res > 0:
                    max_full_gain[q_idx] = res

        cand_z_left_ends = [c['z_left_end'] for c in candidates]
        cand_z_right_starts = [c['z_right_start'] for c in candidates]

        for q_idx, (l, r) in enumerate(queries):
            best_gain = max_full_gain[q_idx]

            # Binary search for candidates overlapping with [l, r]
            low = bisect_left(cand_z_left_ends, l)
            high = bisect_right(cand_z_right_starts, r) - 1

            if low <= high:
                check_indices = set()
                for k in range(low, min(low + 3, high + 1)):
                    check_indices.add(k)
                for k in range(max(low, high - 2), high + 1):
                    check_indices.add(k)

                for idx in check_indices:
                    c = candidates[idx]
                    z_left_contrib = min(c['z_left_end'] - l + 1, c['z_left_end'] - c['z_left_start'] + 1)
                    z_right_contrib = min(r - c['z_right_start'] + 1, c['z_right_end'] - c['z_right_start'] + 1)
                    best_gain = max(best_gain, z_left_contrib + z_right_contrib)

            ans[q_idx] = total_ones_in_s + best_gain

        return ans