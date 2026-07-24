class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int mx = 0;
        for (int x : nums) {
            mx = Math.max(mx, x);
        }
        mx <<= 1;

        boolean[] pair = new boolean[mx];

        for (int a : nums) {
            for (int b : nums) {
                pair[a ^ b] = true;
            }
        }

        boolean[] ans = new boolean[mx];

        for (int x = 0; x < mx; x++) {
            if (!pair[x]) continue;

            for (int c : nums) {
                ans[x ^ c] = true;
            }
        }

        int count = 0;
        for (boolean v : ans) {
            if (v) count++;
        }

        return count;
    }
}