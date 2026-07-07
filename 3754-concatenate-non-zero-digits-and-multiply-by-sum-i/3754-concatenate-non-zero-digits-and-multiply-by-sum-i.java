class Solution {
    public long sumAndMultiply(int n) {
        long x = 0;
        int sum = 0;

        String s = String.valueOf(n);

        for (char c : s.toCharArray()) {
            if (c != '0') {
                x = x * 10 + (c - '0');
                sum += c - '0';
            }
        }

        return x * sum;
    }
}