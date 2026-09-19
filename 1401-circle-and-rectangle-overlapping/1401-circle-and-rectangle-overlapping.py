class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):

        # Closest x-coordinate in the rectangle
        closest_x = max(x1, min(xCenter, x2))

        # Closest y-coordinate in the rectangle
        closest_y = max(y1, min(yCenter, y2))

        # Distance squared from circle center
        dx = closest_x - xCenter
        dy = closest_y - yCenter

        # Avoid sqrt by comparing squared distances
        return dx * dx + dy * dy <= radius * radius