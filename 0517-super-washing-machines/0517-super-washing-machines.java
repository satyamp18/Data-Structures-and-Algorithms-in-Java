class Solution {
    public int findMinMoves(int[] machines) {
        int total = 0;

        for (int x : machines) {
            total += x;
        }

        int n = machines.length;

        if (total % n != 0) {
            return -1;
        }

        int avg = total / n;
        int balance = 0;
        int ans = 0;

        for (int x : machines) {
            int diff = x - avg;
            balance += diff;
            ans = Math.max(ans, Math.max(Math.abs(balance), diff));
        }

        return ans;
    }
}