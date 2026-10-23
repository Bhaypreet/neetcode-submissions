# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        temp = head
        while(temp):
            lis.append(temp.val)
            temp = temp.next

        maxi = lis[-1]
        ans = [maxi]
        for i in range(len(lis)-2,-1,-1):
            if lis[i] >= maxi:
                ans.append(lis[i])
                maxi = max(maxi,lis[i])

        ans.reverse()
        head1 = ListNode(ans[0])
        temp1 = head1

        for i in range(1,len(ans)):
            temp1.next = ListNode(ans[i])
            temp1 = temp1.next

        return head1