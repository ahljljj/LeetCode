/*
503. Next Greater Element II

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

*/

// cpp, stack

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        stack<int> s; unordered_map<int, int> m;
        for (int i = nums.size() - 1; i > -1; --i){
            if (s.empty()){
                m[i] = -1; s.push(i);
                continue;
            }
            if (nums[i] < nums[s.top()]) m[i] = s.top();
            else{
                while (!s.empty() && nums[i] >= nums[s.top()]) s.pop();
                if (s.empty()) m[i] = -1;
                else m[i] = s.top();
            }
            s.push(i);
        }
        for (int i = nums.size() - 1; i > -1; --i){
            if (m[i] != -1) continue;
            if (s.empty()){
                m[i] = -1; s.push(i);
                continue;
            }
            if (nums[i] < nums[s.top()]) m[i] = s.top();
            else{
                while (!s.empty() && nums[i] >= nums[s.top()]) s.pop();
                if (s.empty()) m[i] = -1;
                else m[i] = s.top();
            }
            s.push(i);
        }
        vector<int> res;
        for (int i = 0; i < nums.size(); ++i){
            if (m[i] == -1) res.push_back(-1);
            else res.push_back(nums[m[i]]);
        }
        return res;

    }
};