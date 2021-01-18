# 1618. Maximum Font to Fit a Sentence in a Screen

# 2021/01/07, bineary search over solution space

# Runtime: 748 ms, faster than 10.20% of Python3 online submissions for Maximum Font to Fit a Sentence in a Screen.
# Memory Usage: 25.6 MB, less than 63.27% of Python3 online submissions for Maximum Font to Fit a Sentence in a Screen.

# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
# class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
#
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        l, r = 0, len(fonts) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if not self.check_validity(text, w, h, fonts[m], fontInfo):
                r = m
            else:
                l = m
        if self.check_validity(text, w, h, fonts[r], fontInfo):
            return fonts[r]
        if self.check_validity(text, w, h, fonts[l], fontInfo):
            return fonts[l]
        return -1

    def check_validity(self, text, w, h, font_size, fontInfo):
        curr_w = 0
        for t in text:
            curr_w += fontInfo.getWidth(font_size, t)
        curr_h = fontInfo.getHeight(font_size)
        if curr_w <= w and curr_h <= h:
            return True
        return False
