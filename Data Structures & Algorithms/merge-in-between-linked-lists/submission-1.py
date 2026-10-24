# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        lis1 = []
        lis2 = []

        temp1 = list1
        temp2 = list2

        while(temp1):
            lis1.append(temp1.val)
            temp1 = temp1.next
        while(temp2):
            lis2.append(temp2.val)
            temp2 = temp2.next

        lis3 = lis1[:a]+lis2+lis1[b+1:]

        head = ListNode(lis3[0])
        temp = head
        for i in range(1,len(lis3)):
            temp.next = ListNode(lis3[i])
            temp = temp.next

        return head