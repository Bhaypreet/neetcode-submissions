# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lis = []
        temp = head
        while(temp):
            lis.append(temp.val)
            temp = temp.next

        l = len(lis)
        nlis = []
        
        for i in range(0,len(lis),k):
            if (len(lis)-i)//k >= 1 :
                newlis = lis[i:i+k]
                newlis.reverse()
                nlis+=newlis
            else:
                nlis+=lis[i:len(lis)]

        head1 = ListNode(nlis[0])
        temp1 = head1

        for i in range(1,len(nlis)):
            temp1.next = ListNode(nlis[i])
            temp1 = temp1.next
        return head1