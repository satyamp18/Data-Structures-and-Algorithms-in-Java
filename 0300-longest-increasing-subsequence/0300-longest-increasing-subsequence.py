import bisect

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = []

        for num in nums:
            idx = bisect.bisect_left(lis, num)

            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num

        return len(lis)