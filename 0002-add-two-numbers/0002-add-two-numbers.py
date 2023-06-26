# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: 
        Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newlist=yenilist=ListNode(0)
        value=0
        while l1 or l2:
            if not l1: l1=ListNode(0)
            if not l2: l2=ListNode(0) 
            sum= l1.val+ l2.val+value
            newlist.val=sum%10
            value=sum//10
            print(newlist.val)
            l1=l1.next
            l2=l2.next
            if l1 or l2 or value:
                newlist.next=ListNode(value)
                newlist=newlist.next
        return yenilist