"""
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.


"""


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        nums.sort(key=LargerNumKey)

        return '0' if ''.join(nums)[0] == '0' else ''.join(nums)


# cpp, string sort, rewrite

'''
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int a, int b){return to_string(a) + to_string(b) > to_string(b) + to_string(a);});
        string res;
        for (int &num: nums) res += to_string(num);
        return res[0] != '0'? res: "0";
        
    }
};
'''
