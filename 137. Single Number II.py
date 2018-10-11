"""
137. Single Number II


Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99


"""

'''
Here is some intuition to help understand this nice and concise solution:

First of all, consider the (set^val) as one of the following:
1. adding "val" to the "set" if "val" is not in the "set" => A^0 = A
2. removing "val" from the "set" if "val" is already in the "set" => A^A = 0

Assume "ones" and "twos" to be sets that are keeping track of which numbers have appeared once and twice respectively;

"(ones ^ A[i]) & ~twos" basically means perform the above mentioned operation if and only if A[i] is not present in the set "twos". So to write it in layman:

   IF the set "ones" does not have A[i]
       Add A[i] to the set "ones" if and only if its not there in set "twos"
   ELSE
       Remove it from the set "ones"
So, effectively anything that appears for the first time will be in the set. Anything that appears a second time will be removed. We'll see what happens when an element appears a third time (thats handled by the set "twos").

After this, we immediately update set "twos" as well with similar logic:
"(twos^ A[i]) & ~ones" basically means:

   IF the set "twos" does not have A[i]
       Add A[i] to the set "twos" if and only if its not there in set "ones"
   ELSE
       Remove it from the set "twos"
So, effectively, any number that appears a first time will be in set "ones" so it will not be added to "twos". Any number appearing a second time would have been removed from set "ones" in the previous step and will now be added to set "twos". Lastly, any number appearing a third time will simply be removed from the set "twos" and will no longer exist in either set.

Finally, once we are done iterating over the entire list, set "twos" would be empty and set "ones" will contain the only number that appears once.

'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones
#            print("ones ", ones, "twos ", twos)
        return ones