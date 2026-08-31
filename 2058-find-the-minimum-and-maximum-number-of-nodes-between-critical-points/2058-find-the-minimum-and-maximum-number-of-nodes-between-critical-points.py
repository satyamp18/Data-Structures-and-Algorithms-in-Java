class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        minDistance = float('inf')

        while curr.next:
            # Check local maxima or local minima
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = index
                else:
                    minDistance = min(minDistance, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Less than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        maxDistance = last - first

        return [minDistance, maxDistance]