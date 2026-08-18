class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        int[] sum = new int[n - k + 1];

        int window = 0;
        for (int i = 0; i < n; i++) {
            window += nums[i];

            if (i >= k) {
                window -= nums[i - k];
            }

            if (i >= k - 1) {
                sum[i - k + 1] = window;
            }
        }

        int m = sum.length;

        int[] left = new int[m];
        int best = 0;

        for (int i = 0; i < m; i++) {
            if (sum[i] > sum[best]) {
                best = i;
            }
            left[i] = best;
        }

        int[] right = new int[m];
        best = m - 1;

        for (int i = m - 1; i >= 0; i--) {
            if (sum[i] >= sum[best]) {
                best = i;
            }
            right[i] = best;
        }

        int[] ans = new int[3];
        int maxSum = -1;

        for (int mid = k; mid < m - k; mid++) {
            int l = left[mid - k];
            int r = right[mid + k];

            int total = sum[l] + sum[mid] + sum[r];

            if (total > maxSum) {
                maxSum = total;
                ans[0] = l;
                ans[1] = mid;
                ans[2] = r;
            }
        }

        return ans;
    }
}