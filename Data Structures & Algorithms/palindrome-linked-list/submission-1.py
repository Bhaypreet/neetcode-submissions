# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lis = []
        temp = head
        while(temp):
            lis.append(temp.val)
            temp = temp.next
        l = 0
        r = len(lis)-1
        while(l<=r):
            if lis[l] != lis[r]:
                return False
            l+=1
            r-=1

        return True 