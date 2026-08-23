# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #reverse the list
        cur, last = head, None;
        while cur:
            tmp = cur.next;
            cur.next = last;
            last = cur;
            cur = tmp;
        head = last;
        #remove the nth element
        if n == 1:
            head = head.next;
        else:
            curr = head;
            for _ in range(n - 2):
                curr = curr.next;
            curr.next = curr.next.next;
        #reverse the list
        cur, last = head, None;
        while cur:
            tmp = cur.next;
            cur.next = last;
            last = cur;
            cur = tmp;
        return last;


