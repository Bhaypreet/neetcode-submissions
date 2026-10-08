# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        lis = []
        temp1 = list1
        temp2 = list2

        while(temp2):
            lis.append(temp2.val)
            temp2 = temp2.next
        while(temp1):
            lis.append(temp1.val)
            temp1 = temp1.next
        
        lis.sort()
        if not lis:
            return 
        a = ListNode(lis[0])
        temp = a
        for i in range(1,len(lis)):
            temp.next = ListNode(lis[i])
            temp = temp.next

        return a
        