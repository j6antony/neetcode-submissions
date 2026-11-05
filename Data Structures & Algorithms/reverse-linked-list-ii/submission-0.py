# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
       # 1. Create a dummy node that points to head to safely handle edge cases (like left = 1)
        dummy = ListNode(0, head)
        prev = dummy
        
        # 2. Move 'prev' to the node just before the 'left' position
        for _ in range(left - 1):
            prev = prev.next
            
        cur = prev.next
        node_prev = None
        
        # 3. Reverse the sublist
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = node_prev
            node_prev = cur
            cur = temp
            
        # 4. Reconnect the reversed portion
        prev.next.next = cur
        prev.next = node_prev
        
        return dummy.next