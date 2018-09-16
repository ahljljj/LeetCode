'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

#  Time Limit Exceeded

'''
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    temp=list(range(1,len(nums)+1))
    for num in nums:
        if num in temp:
            temp.remove(num)
    return temp
'''



'''
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    list=[]
    for i in range(1,len(nums)+1):
        if i not in nums:
            list.append(i)
    return list
'''

## one line solution
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
#    temp=list(range(1,len(nums)+1))
    return (set(range(1,len(nums)+1))-set(nums))


'''
list2=[4,3,2,7,8,2,3,1]

print(findDisappearedNumbers(list2))
'''
