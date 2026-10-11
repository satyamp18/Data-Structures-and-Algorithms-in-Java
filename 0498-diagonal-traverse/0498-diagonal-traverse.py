class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m + n - 1):
            diagonal = []

            r = max(0, d - n + 1)
            c = d - r

            while r < m and c >= 0:
                diagonal.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)

        return result