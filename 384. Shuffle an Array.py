"""
384. Shuffle an Array


Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();



"""


# brute force time complexity O(n^2)


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.copy = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.copy
        self.copy = self.nums[:]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        aux = self.nums[:]
        for i in range(len(self.nums)):
            idx = random.randint(0, len(aux) - 1)
            self.nums[i] = aux.pop(idx)
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()





'''

Approach #2 Fisher-Yates Algorithm [Accepted]
Intuition

We can cut down the time and space complexities of shuffle with a bit of cleverness - namely, by swapping elements around within the array itself, we can avoid the linear space cost of the auxiliary array and the linear time cost of list modification.

Algorithm

The Fisher-Yates algorithm is remarkably similar to the brute force solution. On each iteration of the algorithm, 
we generate a random integer between the current index and the last index of the array. Then, we swap the elements at the current index and the chosen index - this simulates drawing (and removing) the element from the hat, as the next range from which we select a random index will not include the most recently processed one. One small, yet important detail is that it is possible to swap an element with 09itself - otherwise, some array permutations would be more likely than others. 



Complexity Analysis

Time complexity : O(n)O(n)

The Fisher-Yates algorithm runs in linear time, as generating a random index and swapping two values can be done in constant time.

Space complexity : O(n)O(n)

Although we managed to avoid using linear space on the auxiliary array from the brute force approach, we still need it for reset, so we're stuck with linear space complexity.

'''





class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.copy = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.copy
        self.copy = self.nums[:]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = len(self.nums)
        for i in range(n):
            idx = random.randint(0, n - i - 1)
            self.nums[i], self.nums[i + idx] = self.nums[i + idx], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()