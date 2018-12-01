"""
418. Sentence Screen Fitting

Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.


"""

# brute force with memorization

'''
I use num to represent how many words can be put in the screen. we use a map<i, cnt> to record for each line how many words cnt can be put when starting with word i. So when we scan each line of the screen, we first get the starting word should be put on this line. If this starting words is already in the map, then just read it; otherwise, create a new entry in this map.

'''

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        count = 0
        tmp = count
        i = 0
        prevLen = 0
        memo = {}
        while i < rows:
            k = 0
            while k in range(len(sentence)):
                word = sentence[k]
                if i >= rows:
                    break
                if prevLen == 0:
                    if word not in memo:
                        start = word
                    else:
                        count += memo[word]
                        k = (k + memo[word]) % len(sentence)
                        i += 1
                        prevLen = 0
                        tmp = count
                        continue
                if len(word) <= cols - prevLen:
                    prevLen += len(word) + 1
                    k += 1
                    count += 1
                else:
                    memo[start] = count - tmp
                    i += 1 # new row
                    prevLen = 0 # reset the length
                    tmp = count
        return count // len(sentence)

# brilliant idea

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = " ".join(sentence) + " "
        start = 0
        for i in range(rows):
            start += cols
            if s[start % len(s)] == " ":
                start += 1
            else:
                while start > 0 and s[(start - 1) % len(s)] != " ":
                    start -= 1
        return start // len(s)

