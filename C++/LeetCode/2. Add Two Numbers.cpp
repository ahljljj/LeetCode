/*
 * 2. Add Two Numbers
 * 
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

 You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 Example:
 Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 Output: 7 -> 0 -> 8
 Explanation: 342 + 465 = 807.
 * 
 * */


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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode res{0}, *curr = &res;
        int extra{0};
        while (l1!= NULL && l2 != NULL){
            int sum{l1->val + l2->val + extra};
            extra = sum / 10;
            sum %= 10;
            curr->next = new ListNode(sum);
            curr = curr->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while (l1 != NULL){
            int sum{l1->val + extra};
            extra = sum / 10;
            sum %= 10;
            curr->next = new ListNode(sum);
            curr = curr->next;
            l1 = l1->next;            
        }
        while (l2 != NULL){
        int sum{l2->val + extra};
        extra = sum / 10;
        sum %= 10;
        curr->next = new ListNode(sum);
        curr = curr->next;
        l2 = l2->next;            
        }        
        if (extra) curr->next = new ListNode(extra);        
        return res.next;        
    }
};