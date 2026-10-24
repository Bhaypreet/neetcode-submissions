# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        ans = 0

        temp = head
        while(temp):
            if temp.val != 0:
                ans+=temp.val
            else:
                if ans!=0 :
                    lis.append(ans)
                    ans = 0
            temp = temp.next

        head1 = ListNode(lis[0])
        temp1 = head1

        for i in range(1,len(lis)):
            temp1.next = ListNode(lis[i])
            temp1 = temp1.next

        return head1