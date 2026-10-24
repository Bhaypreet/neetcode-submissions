# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        x = 0
        while(x<a-1):
            temp1 = temp1.next
            x+=1
        temp3 = temp1
        y = a
        while(y <= b+1):
            temp3 = temp3.next
            y+=1


        temp1.next = temp2 
        while(temp2.next):
            temp2 = temp2.next
        
        temp2.next = temp3
        while(temp3):
            temp3 = temp3.next

        return list1