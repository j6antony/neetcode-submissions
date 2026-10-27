# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        currl1 = l1
        currl2 = l2
        last = None
        while currl1 or currl2 or carry != 0:
            if currl1 and currl2:
                total = currl1.val + currl2.val + carry
                currl1 = currl1.next
                currl2 = currl2.next
            elif currl1:
                total = currl1.val + carry
                currl1 = currl1.next
            elif currl2:
                total = currl2.val + carry
                currl2 = currl2.next
            else:
                total = carry

            if not last:
                last = ListNode(total%10, None)
                head = last
            else:
                last.next =  ListNode(total%10, None)
                last = last.next
            carry = total//10

        return head


        
            
                
                

