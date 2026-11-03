# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        first  = ""
        second = ""
        while l1:
            first += (str(l1.val))
            l1 = l1.next
        while l2:
            second += (str(l2.val))
            l2 = l2.next
        total = int(first) + int(second)
        
        start = ListNode(0)
        final = start 
        for x in (str(total)):
            final.next = ListNode(int(x))
            final = final.next
        return start.next
            
            
            
        
            
            
