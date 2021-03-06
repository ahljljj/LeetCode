"""
451. Sort Characters By Frequency


Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

# hashtable
# time complexity O(nlgn)

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        res = ""
        for (key, val) in dic:
            res += key * val
        return res

# hashmap + heap

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        heap = []
        heapq.heapify(heap)
        for (key, val) in dic.items():
            heapq.heappush(heap, [-val, key])
        res = ''
        while heap:
            (freq, ch) = heapq.heappop(heap)
            res += ch * (-freq)
        return res



# bucket
# time complexity O(n)
'''
The logic is very similar to NO.347 and here we just use a map a count and according to the frequency to put it into the right bucket. Then we go through the bucket to get the most frequently character and append that to the final stringbuilder.

'''

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        buckets = {}
        for (ch, freq) in dic.items():
            if freq not in buckets:
                buckets[freq] = ch * freq
            else:
                buckets[freq] += ch * freq
        res = ''
        for i in range(len(s), -1, -1):
            if i in buckets:
                res += buckets[i]
        return res


