"""
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#merge sort

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        middle_node = self.find_middle_node(head)
        right_head = middle_node.next
        middle_node.next = None
        return self.merge(self.sortList(head), self.sortList(right_head))

    def find_middle_node(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, head1, head2):
        dummy = ListNode(None)
        node = dummy
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next

        node.next = head1 or head2
        return dummy.next

# cpp, rewrite

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
    ListNode* sortList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode * mid = findMid(head);
        ListNode * rightHead = mid->next;
        mid->next = nullptr;
        return merge(sortList(head), sortList(rightHead));
        
    }
    
    ListNode* findMid(ListNode* head){
        ListNode *slow = head, *fast = head;
        while (fast && fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
    ListNode* merge(ListNode* h1, ListNode* h2){
        ListNode* head = new ListNode(-1);
        ListNode* node = head;
        while (h1 && h2){
            if (h1->val < h2->val){
                node->next = h1;
                h1 = h1->next;
            }else{
                node->next = h2;
                h2 = h2->next;
            }
            node = node->next;
        }
        if (h1) node->next = h1;
        else node->next = h2;
        return head->next;
        
    }
    
    
};
'''