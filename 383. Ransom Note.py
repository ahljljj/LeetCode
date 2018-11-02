"""
383. Ransom Note


Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""


# two dictionary space complexity O(n + m)
# time complexity = O(max(m,n))


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        for c in ransomNote:
            dict1[c] = dict1.get(c, 0) + 1
        for c in magazine:
            dict2[c] = dict2.get(c, 0) + 1
        for key in dict1:
            if key not in dict2 or dict1[key] > dict2[key]:
                return False
        return True

# non-dictionary fast

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                magazine = magazine.replace(c, "", 1)
        return True


