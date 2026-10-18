# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lis = []
        temp = head
        
        while(temp is not None):
            lis.append(temp.val)
            temp = temp.next

        l = left-1
        r = right-1

        while(l <=r):
            lis[l],lis[r] = lis[r],lis[l]
            l+=1
            r-=1
        
        head1 = ListNode(lis[0])
        temp1 = head1

        for i in range(1,len(lis)):
            a = ListNode(lis[i])
            temp1.next = a
            temp1 = temp1.next
        return head1