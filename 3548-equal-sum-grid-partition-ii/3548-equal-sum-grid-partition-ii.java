import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // Check horizontal cuts
        if (canPartitionHorizontal(grid, m, n)) {
            return true;
        }

        // Check vertical cuts via transposition
        int[][] transposed = new int[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                transposed[j][i] = grid[i][j];
            }
        }

        return canPartitionHorizontal(transposed, n, m);
    }

    private boolean canPartitionHorizontal(int[][] grid, int m, int n) {
        long totalSum = 0;
        long[] rowSums = new long[m];
        Map<Long, Integer> bottomCounts = new HashMap<>();
        Map<Long, Integer> topCounts = new HashMap<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                long val = grid[i][j];
                rowSums[i] += val;
                bottomCounts.put(val, bottomCounts.getOrDefault(val, 0) + 1);
            }
            totalSum += rowSums[i];
        }

        long topSum = 0;

        for (int r = 0; r < m - 1; r++) {
            topSum += rowSums[r];
            long bottomSum = totalSum - topSum;

            // Shift row r from bottomCounts to topCounts
            for (int c = 0; c < n; c++) {
                long val = grid[r][c];
                
                int bCount = bottomCounts.get(val);
                if (bCount == 1) {
                    bottomCounts.remove(val);
                } else {
                    bottomCounts.put(val, bCount - 1);
                }

                topCounts.put(val, topCounts.getOrDefault(val, 0) + 1);
            }

            // Case 1: Equal without discounting
            if (topSum == bottomSum) {
                return true;
            }

            // Case 2: Discount a cell from the Top section
            if (topSum > bottomSum) {
                long diff = topSum - bottomSum;
                if (n == 1) {
                    // 1D vertical column: only top or bottom endpoint of top-section
                    if (r > 0 && (grid[0][0] == diff || grid[r][0] == diff)) {
                        return true;
                    }
                } else {
                    // 1D row: only endpoints
                    if (r == 0) {
                        if (grid[0][0] == diff || grid[0][n - 1] == diff) {
                            return true;
                        }
                    } else {
                        // 2D subgrid (>= 2x2): any cell removal keeps connectivity
                        if (topCounts.containsKey(diff)) {
                            return true;
                        }
                    }
                }
            }

            // Case 3: Discount a cell from the Bottom section
            if (bottomSum > topSum) {
                long diff = bottomSum - topSum;
                if (n == 1) {
                    // 1D vertical column: only endpoints of bottom-section
                    if (r < m - 2 && (grid[r + 1][0] == diff || grid[m - 1][0] == diff)) {
                        return true;
                    }
                } else {
                    // 1D row: only endpoints
                    if (r == m - 2) {
                        if (grid[m - 1][0] == diff || grid[m - 1][n - 1] == diff) {
                            return true;
                        }
                    } else {
                        // 2D subgrid (>= 2x2): any cell removal keeps connectivity
                        if (bottomCounts.containsKey(diff)) {
                            return true;
                        }
                    }
                }
            }
        }

        return false;
    }
}