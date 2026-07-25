class Solution {
    public int maxProduct(int[] nums) {

        int largest = -1;
        int secondLargest = -1;

        for (int num : nums) {

            if (num >= largest) {
                secondLargest = largest;
                largest = num;
            } else if (num > secondLargest) {
                secondLargest = num;
            }
        }

        return (largest - 1) * (secondLargest - 1);
    }
}