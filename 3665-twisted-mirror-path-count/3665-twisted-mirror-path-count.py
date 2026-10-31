class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # right[i][j]: ways entering (i,j) from the left
        # down[i][j]: ways entering (i,j) from above
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # Start at (0,0)
        right[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ways = 1
                else:
                    ways = (right[i][j] + down[i][j]) % MOD

                if grid[i][j] == 0:
                    # Empty cell: move right or down
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + ways
                        ) % MOD

                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + ways
                        ) % MOD

                else:
                    # Mirror: horizontal entry redirects down
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + right[i][j]
                        ) % MOD

                    # Mirror: vertical entry redirects right
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + down[i][j]
                        ) % MOD

        return (right[m - 1][n - 1] +
                down[m - 1][n - 1]) % MOD