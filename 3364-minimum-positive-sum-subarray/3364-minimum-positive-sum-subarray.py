from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n = len(nums)
        
        # Check every possible starting index
        for i in range(n):
            current_sum = 0
            # Check every possible length from l to r
            for length in range(1, r + 1):
                j = i + length - 1
                if j >= n:
                    break
                
                # Compute sum for the subarray starting at i and ending at j
                if length == 1:
                    current_sum = nums[i]
                else:
                    current_sum += nums[j]
                
                # Consider only if length is within [l, r] and sum is positive
                if length >= l and current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
        return min_sum if min_sum != float('inf') else -1