class Solution {
    public int maxPoints(int[][] points) {
        int n = points.length;
        if (n <= 2) return n;

        int ans = 0;

        for (int i = 0; i < n; i++) {
            Map<String, Integer> map = new HashMap<>();
            int same = 1;

            for (int j = i + 1; j < n; j++) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                if (dx == 0 && dy == 0) {
                    same++;
                    continue;
                }

                int g = gcd(Math.abs(dx), Math.abs(dy));
                dx /= g;
                dy /= g;

                if (dx < 0) {
                    dx = -dx;
                    dy = -dy;
                } else if (dx == 0) {
                    dy = 1;
                } else if (dy == 0) {
                    dx = 1;
                }

                String key = dx + "#" + dy;
                map.put(key, map.getOrDefault(key, 0) + 1);
            }

            ans = Math.max(ans, same);

            for (int count : map.values()) {
                ans = Math.max(ans, count + same);
            }
        }

        return ans;
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