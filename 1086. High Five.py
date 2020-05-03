'''
1086. High Five

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.



Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.


Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
Accepted
21,904
Submissions
28,009

'''

# 2020/05/02, brute force, hashtable + sort

'''
Runtime: 72 ms, faster than 81.93% of Python3 online submissions for High Five.
Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for High Five.
'''

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = collections.defaultdict(list)
        for i, score in items:
            scores[i].append(score)
        res = []
        for i in scores:
            n = min(5, len(scores[i]))
            avg = sum(sorted(scores[i], reverse=True)[:n]) // n
            res.append([i, avg])
        return sorted(res)


