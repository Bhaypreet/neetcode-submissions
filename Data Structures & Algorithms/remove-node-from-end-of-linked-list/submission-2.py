# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        lis = []
        temp = head

        while(temp is not None):
            lis.append(temp.val)
            temp = temp.next

        

        lis.pop(len(lis)-n)

        if len(lis) == 0:
            return None

        head1 = ListNode(lis[0])
        temp1 = head1

        for i in range(1,len(lis)):
            temp1.next = ListNode(lis[i])
            temp1 = temp1.next
        
        return head1
