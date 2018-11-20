"""

434. Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5



"""

# for loop

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = 0
        n = len(s)
        while i < n and s[i] == " ":
            i += 1
        while i < n:
            while i < n and s[i] != " ":
                i += 1
            count += 1
            while i < n and s[i] == " ":
                i += 1
        return count

