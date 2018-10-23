"""
313. Super Ugly Number


Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

"""


# dynamic programming

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        m = len(primes)
        idx = [0] * m
        ugly = [1] * n
        for i in range(1, n):
            ugly[i] = float("inf")
            for j in range(m):
                tmp = ugly[idx[j]] * primes[j]
                if tmp < ugly[i]:
                    ugly[i] = tmp
            for j in range(m):
                if ugly[i] == ugly[idx[j]] * primes[j]:
                    idx[j] += 1
        return ugly[-1]


'''
# python heap: TLE time complexity: O(nlgn)


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        res = None
        k = 0
        while k < n:
            i = heapq.heappop(ugly)
            if i == res: continue
            res = i
            for prime in primes:
                heapq.heappush(ugly, i * prime)
            k += 1
        return res
                



'''