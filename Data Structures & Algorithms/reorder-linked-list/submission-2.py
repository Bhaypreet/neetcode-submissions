# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lis = []
        temp = head
        while(temp is not None):
            lis.append(temp.val)
            temp = temp.next


        if len(lis) <= 2:
            return 
        flis = []
        l = 0
        r = len(lis)-1
        while(l <=r):
            flis.append(lis[l])
            l+=1
            if l <= r :
                flis.append(lis[r])
                r-=1


        temp1 = head
        for i in range(1,len(flis)):
            a = ListNode(flis[i])
            temp1.next = a
            temp1 = temp1.next

        temp1.next = None

        
            