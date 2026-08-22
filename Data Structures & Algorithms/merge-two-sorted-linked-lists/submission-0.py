# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1;
        curr2 = list2;
        head = None;
        if curr1 and curr2:
            if curr1.val >= curr2.val:
                head = curr2;
                curr2 = curr2.next;
            else:
                head = curr1;
                curr1 = curr1.next;
        elif curr1:
            return curr1;
        else:
            return curr2;
        front = head;
        while curr1 and curr2:
            print(curr1.val, curr2.val);
            if curr1.val >= curr2.val:
                head.next = curr2
                head = head.next;
                curr2 = curr2.next;
            else:
                head.next = curr1
                head = head.next;
                curr1 = curr1.next;
        if curr1:
            head.next = curr1;
        else:
            head.next = curr2;
        return front;
        


