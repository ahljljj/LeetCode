/*
473. Matchsticks to Square

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.


*/

// cpp, dfs

class Solution {
public:
    bool makesquare(vector<int>& nums) {
        if (nums.empty()) return false;
        vector<int> sums(4, 0);
        int sum = 0;
        for (int num: nums) sum += num;
        if (sum %4 != 0) return false;
        int length = nums.size(), mean = sum / 4;
        sort(nums.begin(), nums.end(), greater<int>());
        return dfs(sums, nums, length, mean, 0);

    }

    bool dfs(vector<int> & sums, vector<int> & nums, int length, int mean, int idx){
        if (idx == length) return (sums[0] == mean && sums[1] == mean && sums[2] == mean);
        for (int i = 0; i < 4; ++i){
            if (sums[i] + nums[idx] <= mean){
                sums[i] += nums[idx];
                if (dfs(sums, nums, length, mean, idx + 1)) return true;
                sums[i] -= nums[idx];
            }
        }
        return false;

    }
};


/*
Runtime: 76 ms, faster than 89.79% of Python3 online submissions for Matchsticks to Square.
Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Matchsticks to Square.


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        perimeter = sum(nums)
        size = perimeter // 4
        if perimeter % 4 != 0 or max(nums) > size: return False
        self.res = 0
        nums.sort(reverse = True)
        self.dfs(nums, size, set(), 0, set())
        return self.res == 4

    def dfs(self, nums, size, subset, pos, visited):
        if size == 0:
            # intersection is none
            if not subset & visited:
                # union
                visited |= subset
                self.res += 1
            return
        if pos == len(nums) or size < 0:
            return
        for i in range(pos, len(nums)):
            subset.add(i)
            self.dfs(nums, size - nums[i], subset, i + 1, visited)
            subset.remove(i)


*/