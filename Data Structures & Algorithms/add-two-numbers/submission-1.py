# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        temp1 = l1
        temp2 = l2

        lis1 = []
        lis2 = []
        
        while(temp1):
            lis1.append(temp1.val)
            temp1 = temp1.next
        
        while(temp2):
            lis2.append(temp2.val)
            temp2 = temp2.next
        
        lis3 = []

        i = 0
        j = 0
        c = 0

        while(i<len(lis1) or j < len(lis2)):

            a = 0
            b = 0
            if i < len(lis1):
                a = lis1[i]
                i+=1
            if j < len(lis2):
                b = lis2[j]
                j +=1
            
            lis3.append((a+b+c)%10)
            c = (a+b+c)//10
                
        if c > 0:
            lis3.append(c)

        head1 = ListNode(lis3[0])
        x = head1

        for i in range(1,len(lis3)):
            y = ListNode(lis3[i])

            x.next = y
            x = x.next
        
        return head1








