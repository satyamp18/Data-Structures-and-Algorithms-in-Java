class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)

        # dp[i][j] = [maximum score, number of paths]
        # Score -1 means the cell is unreachable.
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]

        # Starting position S
        dp[n - 1][n - 1] = [0, 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue

                best = -1
                ways = 0

                # Move up, left, or diagonally up-left
                for ni, nj in (
                    (i + 1, j),
                    (i, j + 1),
                    (i + 1, j + 1)
                ):
                    if ni < n and nj < n:
                        score, count = dp[ni][nj]

                        # Check reachability using score, NOT count
                        if score == -1:
                            continue

                        if score > best:
                            best = score
                            ways = count

                        elif score == best:
                            ways = (ways + count) % MOD

                if best != -1:
                    value = 0 if board[i][j] == 'E' else int(board[i][j])

                    dp[i][j] = [
                        best + value,
                        ways % MOD
                    ]

        # Check reachability using score, not path count
        if dp[0][0][0] == -1:
            return [0, 0]

        return dp[0][0]