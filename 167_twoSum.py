'''
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

'''

# Time exceed limit

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
#        numbers=[i for i in numbers if i<=target]
        nb=len(numbers)
        for i in range(nb):
            for j in range(i+1,nb):
                if target==numbers[i]+numbers[j]:
                    return [i+1,j+1]


#17 / 17 test cases passed. Runtime: 32 ms
#Your runtime beats 18.22% of python 3 submissions.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #        numbers=[i for i in numbers if i<=target]
        nb = len(numbers)
        low = 0
        upper = nb - 1
        while numbers[low] + numbers[upper] != target:
            if numbers[low] + numbers[upper] > target:
                upper = upper - 1
            else:
                low = low + 1
        return [low + 1, upper + 1]

