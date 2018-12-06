"""
249. Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]


"""

# hashtable
# time complexity O(n * maxLen)

class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hMap = {}
        for s in strings:
            tmp = self.strToKey(s)
            if tmp not in hMap:
                hMap[tmp] = [s]
            else:
                hMap[tmp].append(s)
        res = []
        for key in hMap:
            res.append(hMap[key])
        return res

    def strToKey(self, string):
        shift = ord(string[0]) - ord('a')
        tmp = ''
        for s in string:
            tmp += chr(ord('a') + (ord(s) - shift) % 26)
        return tmp

