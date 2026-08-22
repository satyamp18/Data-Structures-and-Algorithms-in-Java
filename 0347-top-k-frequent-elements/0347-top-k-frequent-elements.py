from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        return [x for x, _ in freq.most_common(k)]