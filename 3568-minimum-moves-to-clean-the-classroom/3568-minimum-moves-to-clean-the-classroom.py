from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter = []
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        k = len(litter)

        # No litter
        if k == 0:
            return 0

        litter_id = {pos: i for i, pos in enumerate(litter)}

        # State:
        # (row, col, energy_left, mask)
        #
        # BFS guarantees the first time we reach a state with
        # all litter collected, it is the minimum number of moves.
        q = deque()

        sr, sc = start
        q.append((sr, sc, energy, 0))

        # Store maximum energy reached for each (row, col, mask).
        # If we have already reached the same state with >= energy,
        # the current state is unnecessary.
        best = {}

        best[(sr, sc, 0)] = energy

        moves = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        full_mask = (1 << k) - 1

        while q:
            size = len(q)

            for _ in range(size):
                r, c, e, mask = q.popleft()

                if mask == full_mask:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Need one unit of energy for every move
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[(nr, nc)]
                        nmask |= (1 << idx)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, nmask)

                    # If we've reached this state before with
                    # at least as much energy, this path is useless.
                    if state in best and best[state] >= ne:
                        continue

                    best[state] = ne
                    q.append((nr, nc, ne, nmask))

            moves += 1

        return -1