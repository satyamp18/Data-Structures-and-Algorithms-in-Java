class Solution {
    public int[][] transpose(int[][] matrix) {
        if (matrix == null || matrix.length == 0) {
            return new int[0][0];
        }

        int totalRows = matrix.length;
        int totalCols = matrix[0].length;

        int newTotalRows = totalCols;
        int newTotalCols = totalRows;

        int[][] ans = new int[newTotalRows][newTotalCols];

        for (int row = 0; row < totalRows; row++) {
            for (int col = 0; col < totalCols; col++) {
                ans[col][row] = matrix[row][col];
            }
        }

        return ans;
    }
}