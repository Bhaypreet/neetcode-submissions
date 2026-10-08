# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        a = head
        curr = a
        while(curr is not None):
            b = curr.next
            curr.next = pre
            pre = curr
            curr = b
        return pre
