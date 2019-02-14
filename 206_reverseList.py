'''
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        revlist = []
        while head:
            revlist.append(head)
            head = head.next
        tmp = rev = ListNode(None)
        for r in revlist[::-1]:
            rev.next = r
            rev = rev.next
        rev.next = None
        return tmp.next


# not my idea, but pretty easy

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        curr = head
        prev = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head.next = None
        return prev

#cpp, iterate, rewrite

'''
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return head;
        ListNode * prev = head, *curr = head;
        while (curr){
            ListNode *tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        head->next = nullptr;
        return prev;
        
    }
};
'''

# cpp, recursive solution

'''
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode *p = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return p;
        
    }
};
'''

