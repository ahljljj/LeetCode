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

// cpp, binary search

class Solution {
public:
    bool judgeSquareSum(int c) {
        for (long i = 0; i * i <= c; ++i){
            if (binarySearch(c - i * i)) return true;
        }
        return false;
    }

    bool binarySearch(long target){
        long l = 0, r = target;
        while (l <= r){
            long m = (l + r) >> 1;
            if (m * m == target) return true;
            else if (m * m > target) r = m - 1;
            else l = m + 1;
        }
        return false;
    }
};