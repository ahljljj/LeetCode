"""
406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


"""

# sort by custom comparision function and insertion sort
# slow with time complexity O(n^2)


import functools


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        people = sorted(people, key=functools.cmp_to_key(self.compare))
        for i in range(1, len(people)):
            j = people[i][1]
            move = j - i
            k = i
            if move < 0:
                move = -move
                while move > 0 and k >= 0:
                    people[k], people[k - 1] = people[k - 1], people[k]
                    move -= 1
                    k -= 1
        return people

    def compare(self, pair1, pair2):
        if pair1[0] > pair2[0]:
            return -1
        elif pair1[0] == pair2[0] and pair1[1] < pair2[1]:
            return -1
        else:
            return 1
