class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int total = m * n;

        k %= total;

        List<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            ans.add(new ArrayList<>());
            for (int j = 0; j < n; j++) {
                ans.get(i).add(0);
            }
        }

        for (int i = 0; i < total; i++) {
            int newPos = (i + k) % total;

            int r1 = i / n;
            int c1 = i % n;

            int r2 = newPos / n;
            int c2 = newPos % n;

            ans.get(r2).set(c2, grid[r1][c1]);
        }

        return ans;
    }
}