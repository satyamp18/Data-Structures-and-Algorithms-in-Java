class Solution {
    static final int MOD = 1000000007;
    int[][][] dp;
    int[] nums;
    int n;
    int MAX;

    public int subsequencePairCount(int[] nums) {
        this.nums = nums;
        n = nums.length;

        MAX = 0;
        for (int x : nums) MAX = Math.max(MAX, x);

        dp = new int[n][MAX + 1][MAX + 1];
        for (int i = 0; i < n; i++)
            for (int j = 0; j <= MAX; j++)
                Arrays.fill(dp[i][j], -1);

        return dfs(0, 0, 0);
    }

    private int dfs(int idx, int g1, int g2) {
        if (idx == n) {
            if (g1 != 0 && g1 == g2) return 1;
            return 0;
        }

        if (dp[idx][g1][g2] != -1)
            return dp[idx][g1][g2];

        long ans = dfs(idx + 1, g1, g2);

        int ng1 = g1 == 0 ? nums[idx] : gcd(g1, nums[idx]);
        ans += dfs(idx + 1, ng1, g2);

        int ng2 = g2 == 0 ? nums[idx] : gcd(g2, nums[idx]);
        ans += dfs(idx + 1, g1, ng2);

        return dp[idx][g1][g2] = (int)(ans % MOD);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}