'''
1052. Grumpy Bookstore Owner

Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.



Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1


2020/03/28, sliding window

Runtime: 300 ms, faster than 91.85% of Python3 online submissions for Grumpy Bookstore Owner.
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Grumpy Bookstore Owner.

idea: 1. fixed window size so there is no left pointer in this case. 2. divide the customers into two groups: a)
customers who have already been satisfied, i.e., the corresponding grumpy is 0; b) curstomers who enter at a bad
time, i.e., grumpy[i] = 0. 3. the window captures the number of customers by changing the customers grumpy from 1 to 0.


'''


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # no left pointer since the window size is fixed: X
        r = 0
        max_potential = 0
        already_satisfied = 0
        potential_satisfied = 0
        for r in range(len(customers)):
            if grumpy[r] == 0:
                already_satisfied += customers[r]
            else:
                potential_satisfied += customers[r]
            if r >= X and grumpy[r - X] == 1: potential_satisfied -= customers[r - X]
            max_potential = max(max_potential, potential_satisfied)
        return already_satisfied + max_potential