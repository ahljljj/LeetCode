"""
398. Random Pick Index


Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);



"""


# brute force
# space complexity O(n)


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = {}
        for i in range(len(nums)):
            if nums[i] not in self.nums:
                self.nums[nums[i]] = [i]
            else:
                self.nums[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        lst = self.nums[target]
        idx = random.randint(0, len(lst) - 1)
        return lst[idx]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)



# reservoir sampling
# O(1) space complexity

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        res = None
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                idx = random.randint(0, count - 1)
                if idx == count - 1:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)