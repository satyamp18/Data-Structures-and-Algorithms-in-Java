class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        total = 0

        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]

            total += min(gap, duration)

        # Last attack always contributes full duration
        total += duration

        return total