"""

423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"



"""

# gauss elimination

'''
The idea is:

for zero, it's the only word has letter 'z',
for two, it's the only word has letter 'w',
......
so we only need to count the unique letter of each word, Coz the input is always valid.

'''


class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * 10

        for ch in s:
            if ch == "z": count[0] += 1
            if ch == "w": count[2] += 1
            if ch == "u": count[4] += 1
            if ch == "x": count[6] += 1
            if ch == "g": count[8] += 1

            if ch == "s": count[7] += 1
            if ch == "f": count[5] += 1
            if ch == "o": count[1] += 1
            if ch == "h": count[3] += 1
            if ch == "i": count[9] += 1
        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[1] -= count[0] + count[2] + count[4]
        count[9] -= count[6] + count[8] + count[5]

        res = ""
        for i in range(10):
            if count[i] > 0:
                res += str(i) * count[i]
        return res


