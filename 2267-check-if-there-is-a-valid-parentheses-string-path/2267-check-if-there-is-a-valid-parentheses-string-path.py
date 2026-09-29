class Solution:
    def hasValidPath(self, grid) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # First cell must be '('
        if grid[0][0] == ')':
            return False

        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    dp[j].add(1)
                    continue

                possible = set()

                # From top
                if i > 0:
                    possible.update(dp[j])

                # From left
                if j > 0:
                    possible.update(dp[j - 1])

                change = 1 if grid[i][j] == '(' else -1

                dp[j] = {
                    balance + change
                    for balance in possible
                    if balance + change >= 0
                }

        return 0 in dp[n - 1]