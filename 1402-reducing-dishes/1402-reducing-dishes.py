class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()

        total = 0
        prefix = 0

        # Start from the most satisfying dish
        for i in range(len(satisfaction) - 1, -1, -1):
            prefix += satisfaction[i]

            # Adding this dish is useful only if
            # the total contribution remains positive.
            if prefix > 0:
                total += prefix
            else:
                break

        return total