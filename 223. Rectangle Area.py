"""
223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.


"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        length, width = 0, 0
        if A > E:
            A, B, C, D, E, F, G, H = E, F, G, H, A, B, C, D
        if E >= C or G <= A or F >= D or H <= B:
            return (C - A) * (D - B) + (G - E) * (H - F)
        elif A <= E <= C and B <= F <= D:
            if A <= G <= C:
                length = G - E
            else:
                length = C - E
            if B <= H <= D:
                width = H - F
            else:
                width = D - F
        else:
            if H >= D:
                width = D - B
            else:
                width = H - B
            if A <= G <= C:
                length = G - E
            else:
                length = C - E
        return (C - A) * (D - B) + (G - E) * (H - F) - length * width