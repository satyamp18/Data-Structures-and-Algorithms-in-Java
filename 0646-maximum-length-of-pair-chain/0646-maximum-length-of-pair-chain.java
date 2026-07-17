class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[1], b[1]));

        int ans = 0;
        int end = Integer.MIN_VALUE;

        for (int[] pair : pairs) {
            if (pair[0] > end) {
                ans++;
                end = pair[1];
            }
        }

        return ans;
    }
}