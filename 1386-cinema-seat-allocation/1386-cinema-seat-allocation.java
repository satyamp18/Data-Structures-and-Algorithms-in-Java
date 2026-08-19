import java.util.*;

class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int[] seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];
            map.put(row, map.getOrDefault(row, 0) | (1 << (col - 1)));
        }

        int ans = (n - map.size()) * 2;

        int left = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4);
        int middle = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6);
        int right = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8);

        for (int mask : map.values()) {
            boolean l = (mask & left) == 0;
            boolean m = (mask & middle) == 0;
            boolean r = (mask & right) == 0;

            if (l && r) {
                ans += 2;
            } else if (l || m || r) {
                ans++;
            }
        }

        return ans;
    }
}