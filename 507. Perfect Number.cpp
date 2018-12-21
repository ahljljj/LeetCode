/*
507. Perfect Number

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

*/

// cpp, unsure why cann't pass


class Solution {
public:
    bool checkPerfectNumber(int num) {
        int res, upper = sqrt(num);
        for (int i = 1; i <= upper; ++i){
//            cout << i << " " << res << endl;
            if (i == 1){
                res += 1;
                continue;
            }
            if (num % i == 0){
                int tmp = num / i;
                res += i;
                if (tmp != i) res += tmp;
                if (res > num) return false;
            }
        }
        return res == num;

    }
};