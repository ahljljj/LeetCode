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

'''
The even digits all have a unique letter while the odd digits all don't:

zero: Only digit with z
two: Only digit with w
four: Only digit with u
six: Only digit with x
eight: Only digit with g

The odd ones for easy looking, each one's letters all also appear in other digit words:
one, three, five, seven, nine
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

'''
In general situation, it should be transformed into a problem to calculate A from AX=B, matrix X is formed as follows,
         //                                             /// efghinorstuvwxz ///
        // 0 z e r o        e         o  r            z    100000110000001      
        // 1 o n e          e        no                    100001100000000                      
        // 2 t w o                    o      t    w         000000100100100        
        // 3 t h r e e      e    h       r   t              200100010100000            
        // 4 f o u r          f       o  r     u             010000110010000   
        // 5 f i v e        e f    i             v            110010000001000                   
        // 6 s i x                 i       s        x          000010001000010           
        // 7 s e v e n      e        n     s     v        200001001001000        
        // 8 e i g h t      e  g h i         t              101110000100000   
        // 9 n i n e        e      i n                       100012000000000
				Then we can use math or back tarce method to figure A out.

'''


