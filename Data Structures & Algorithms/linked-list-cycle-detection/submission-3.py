# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        l = head.next
        if l is None:
            return False
        r = head.next.next

        while(r is not None and r.next is not None ):
            if l == r:
                return True
            r = r.next.next
            l = l.next
        
        return False