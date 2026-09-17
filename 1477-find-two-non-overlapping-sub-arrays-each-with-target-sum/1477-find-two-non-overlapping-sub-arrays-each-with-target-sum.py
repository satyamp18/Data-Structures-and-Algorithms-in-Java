class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        INF = float('inf')

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0:i]
        best = [INF] * (n + 1)

        left = 0
        curr_sum = 0
        answer = INF

        for right in range(n):
            curr_sum += arr[right]

            # Since all numbers are positive,
            # shrink the window if sum becomes too large.
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Find a previous non-overlapping subarray.
                # best[left] contains the shortest valid subarray
                # ending before 'left'.
                if best[left] != INF:
                    answer = min(answer, length + best[left])

                # Update best for subarrays ending at 'right'
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if answer == INF else answer