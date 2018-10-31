"""
374. Guess Number Higher or Lower


We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6



"""



# binary search time complexity O(lg2(n))

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                left = mid + 1
            else:
                right = mid - 1


# ternary search

'''
In Binary Search, we choose the middle element as the pivot in splitting. In Ternary Search, we choose two pivots (say m1m1 and m2m2) such that the given range is divided into three equal parts. If the required number numnum is less than m1m1 then we apply ternary search on the left segment of m1m1. If numnum lies between m1m1 and m2m2, we apply ternary search between m1m1 and m2m2. Otherwise we will search in the segment right to m2m2.


follow up

It seems that ternary search is able to terminate earlier compared to binary search. But why is binary search more widely used?

Comparisons between Binary Search and Ternary Search
Ternary Search is worse than Binary Search in the worst case.

T(n) = 2 + T(n/2)

T(n) = 4 + T(n/3)

'''




# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            if guess(mid1) == 0:
                return mid1
            if guess(mid2) == 0:
                return mid2
            if guess(mid1) < 0:
                right = mid1 - 1
            elif guess(mid2) > 0:
                left = mid2 + 1
            else:
                right = mid2 - 1
                left = mid1 + 1

