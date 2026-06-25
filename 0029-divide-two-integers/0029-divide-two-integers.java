class Solution {
    public int divide(int dividend, int divisor) {
        // Handle the specific corner case that causes 32-bit integer overflow
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        // Determine the sign of the final quotient
        boolean isNegative = (dividend < 0) ^ (divisor < 0);

        // Convert both numbers to negative to safely prevent overflow issues
        int absDividend = dividend < 0 ? dividend : -dividend;
        int absDivisor = divisor < 0 ? divisor : -divisor;

        int quotient = 0;

        // Since we are working with negative numbers, "less than or equal to" 
        // means having a larger absolute magnitude (e.g., -10 <= -3)
        while (absDividend <= absDivisor) {
            int tempDivisor = absDivisor;
            int multiple = 1;

            // Double the divisor and the multiple until doubling would exceed the dividend.
            // tempDivisor >= (Integer.MIN_VALUE >> 1) prevents bit-shift overflow.
            while (tempDivisor >= (Integer.MIN_VALUE >> 1) && absDividend <= (tempDivisor << 1)) {
                tempDivisor <<= 1;
                multiple <<= 1;
            }

            // Subtract the largest accumulated divisor from dividend
            absDividend -= tempDivisor;
            // Add the corresponding multiple to the quotient
            quotient += multiple;
        }

        // Return the properly signed quotient
        return isNegative ? -quotient : quotient;
    }
}