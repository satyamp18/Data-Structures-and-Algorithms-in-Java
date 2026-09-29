class Solution:
    def gameOfLife(self, board) -> None:
        m = len(board)
        n = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for i in range(m):
            for j in range(n):

                live_neighbors = 0

                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < m and 0 <= nj < n:
                        # 1 and 2 both represent cells
                        # that were originally alive
                        if board[ni][nj] in (1, 2):
                            live_neighbors += 1

                # Current cell was alive
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2

                # Current cell was dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 3

        # Convert temporary states to final states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1