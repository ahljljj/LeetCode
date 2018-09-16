'''
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


'''

'''
Time limit exceeded

class Solution(object):
    def isprime(self, n):
        for i in range(2,1+int(n**0.5)):
            if n%i==0:
                return False
        return True
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=2
        count=0
        while i<n:
            if self.isprime(i):
                count+=1
            i+=1
        return count
        

'''


class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False

        for i in range(2, 1 + int(n ** 0.5)):
            if primes[i]:
                for j in range(2, (n - 1) // i + 1):
                    primes[i * j] = False
        return sum(primes)
