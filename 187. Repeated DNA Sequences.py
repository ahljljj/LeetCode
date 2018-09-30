"""
187. Repeated DNA Sequences


All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]


"""

'''
wrong

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        hashmap = {}
        n = len(s)
        for i in range(n - 10):
            j = i
            hashmap = {}
            while j < n - 10:
                if s[j:j+10] not in hashmap:
                    hashmap[s[j:j+10]] = 1
                else:
                    hashmap[s[j:j+10]] += 1
                    res.append(s[j:j+10])
                j += 10
            print(hashmap)
        return res
                    
        

'''


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        hashmap = {}
        n = len(s)
        for i in range(n - 9):
            if s[i:i + 10] not in hashmap:
                hashmap[s[i:i + 10]] = True
            elif hashmap[s[i:i + 10]]:
                hashmap[s[i:i + 10]] = False
                res.append(s[i:i + 10])
        return res

