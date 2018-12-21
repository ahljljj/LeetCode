/*
506. Relative Ranks

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

*/

// cpp, pairing and sort

class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        vector<pair<int, int>> table;
        for (int i = 0; i < nums.size(); ++i) table.push_back(make_pair(nums[i], i));
        sort(table.begin(), table.end());
        vector<string> res(nums.size());
        for (int i = table.size() - 1, count = 0; i > -1; --i, ++count){
            if (count == 0) res[table[i].second] = "Gold Medal";
            else if (count == 1) res[table[i].second] = "Silver Medal";
            else if (count == 2) res[table[i].second] = "Bronze Medal";
            else res[table[i].second] = to_string(count + 1);
        }
        return res;

    }
};

# cpp, priority_queue

class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        priority_queue<pair<int, int>> table;
        for (int i = 0; i < nums.size(); ++i) table.push(make_pair(nums[i], i));
        vector<string> res(nums.size());
        for (int i = 0; i < nums.size(); ++i){
            pair<int, int> rank = table.top();
            if (i == 0) res[rank.second] = "Gold Medal";
            else if (i == 1) res[rank.second] = "Silver Medal";
            else if (i == 2) res[rank.second] = "Bronze Medal";
            else res[rank.second] = to_string(i + 1);
            table.pop();
        }
        return res;

    }
};