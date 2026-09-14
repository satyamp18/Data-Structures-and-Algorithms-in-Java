class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        # Overlap on X-axis
        x_overlap = max(x1, a1) < min(x2, a2)

        # Overlap on Y-axis
        y_overlap = max(y1, b1) < min(y2, b2)

        return x_overlap and y_overlap