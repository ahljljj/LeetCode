/*
633. Sum of Square Numbers

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False

*/

//cpp, hashtable

class Solution {

public:
    bool judgeSquareSum(int c) {
        unordered_set<long> set;
        for (long i = 0; i * i <= c; ++i) set.insert(i * i);
        for (long num: set){
            if (set.find(c - num) != set.end()) return true;
        }
        return false;

    }
};