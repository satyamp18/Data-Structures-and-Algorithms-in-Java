import java.util.*;

class Solution {
    public String smallestNumber(String num, long t) {
        long tempT = t;
        int[] target = new int[8]; // Stores counts for 2, 3, 5, 7
        int[] primes = {2, 3, 5, 7};
        
        for (int p : primes) {
            while (tempT % p == 0) {
                target[p]++;
                tempT /= p;
            }
        }
        
        // If t has prime factors other than 2, 3, 5, or 7
        if (tempT > 1) return "-1";

        int[][] digitFactors = {
            {0, 0, 0, 0}, // 0
            {0, 0, 0, 0}, // 1
            {1, 0, 0, 0}, // 2
            {0, 1, 0, 0}, // 3
            {2, 0, 0, 0}, // 4
            {0, 0, 1, 0}, // 5
            {1, 1, 0, 0}, // 6
            {0, 0, 0, 1}, // 7
            {3, 0, 0, 0}, // 8
            {0, 2, 0, 0}  // 9
        };

        int n = num.length();
        int firstZeroIdx = -1;
        int[][] pFactors = new int[n + 1][8];

        for (int i = 0; i < n; i++) {
            int d = num.charAt(i) - '0';
            if (d == 0) {
                firstZeroIdx = i;
                break;
            }
            pFactors[i + 1][2] = pFactors[i][2] + digitFactors[d][0];
            pFactors[i + 1][3] = pFactors[i][3] + digitFactors[d][1];
            pFactors[i + 1][5] = pFactors[i][5] + digitFactors[d][2];
            pFactors[i + 1][7] = pFactors[i][7] + digitFactors[d][3];
        }

        // Case 1: num itself is zero-free and valid
        if (firstZeroIdx == -1) {
            if (pFactors[n][2] >= target[2] && pFactors[n][3] >= target[3] &&
                pFactors[n][5] >= target[5] && pFactors[n][7] >= target[7]) {
                return num;
            }
        }

        int maxPrefixLen = (firstZeroIdx != -1) ? firstZeroIdx : n;

        // Case 2: Try matching prefixes of num
        for (int pLen = maxPrefixLen; pLen >= 0; pLen--) {
            int curr2 = pFactors[pLen][2];
            int curr3 = pFactors[pLen][3];
            int curr5 = pFactors[pLen][5];
            int curr7 = pFactors[pLen][7];
            int remLen = n - pLen;

            int startDigit = (pLen < n) ? (num.charAt(pLen) - '0' + 1) : 10;

            for (int nextDigit = startDigit; nextDigit <= 9; nextDigit++) {
                int req2 = target[2] - (curr2 + digitFactors[nextDigit][0]);
                int req3 = target[3] - (curr3 + digitFactors[nextDigit][1]);
                int req5 = target[5] - (curr5 + digitFactors[nextDigit][2]);
                int req7 = target[7] - (curr7 + digitFactors[nextDigit][3]);

                if (isPossible(remLen - 1, req2, req3, req5, req7)) {
                    StringBuilder sb = new StringBuilder();
                    sb.append(num, 0, pLen);
                    sb.append(nextDigit);
                    sb.append(getSmallestSuffix(remLen - 1, req2, req3, req5, req7, digitFactors));
                    return sb.toString();
                }
            }
        }

        // Case 3: Larger length (n + 1 or more)
        int totalLen = n + 1;
        while (true) {
            if (isPossible(totalLen, target[2], target[3], target[5], target[7])) {
                return getSmallestSuffix(totalLen, target[2], target[3], target[5], target[7], digitFactors);
            }
            totalLen++;
        }
    }

    // Checks if `len` digits can supply at least c2 twos, c3 threes, c5 fives, and c7 sevens
    private boolean isPossible(int len, int c2, int c3, int c5, int c7) {
        c2 = Math.max(0, c2);
        c3 = Math.max(0, c3);
        c5 = Math.max(0, c5);
        c7 = Math.max(0, c7);

        if (c5 + c7 > len) return false;
        int remLen = len - c5 - c7;

        // Try using `num6` sixes (from 0 to min(c2, c3, remLen))
        for (int num6 = 0; num6 <= Math.min(remLen, Math.min(c2, c3)); num6++) {
            int rem2 = c2 - num6;
            int rem3 = c3 - num6;
            int avail = remLen - num6;

            int count8 = (rem2 + 2) / 3;
            int count9 = (rem3 + 1) / 2;

            if (count8 + count9 <= avail) return true;
        }

        return false;
    }

    // Constructs the smallest suffix of length `k`
    private String getSmallestSuffix(int k, int c2, int c3, int c5, int c7, int[][] digitFactors) {
        c2 = Math.max(0, c2);
        c3 = Math.max(0, c3);
        c5 = Math.max(0, c5);
        c7 = Math.max(0, c7);

        StringBuilder suffix = new StringBuilder();

        while (k > 0) {
            for (int d = 1; d <= 9; d++) {
                int nc2 = c2 - digitFactors[d][0];
                int nc3 = c3 - digitFactors[d][1];
                int nc5 = c5 - digitFactors[d][2];
                int nc7 = c7 - digitFactors[d][3];

                if (isPossible(k - 1, nc2, nc3, nc5, nc7)) {
                    suffix.append(d);
                    c2 = nc2;
                    c3 = nc3;
                    c5 = nc5;
                    c7 = nc7;
                    k--;
                    break;
                }
            }
        }

        return suffix.toString();
    }
}