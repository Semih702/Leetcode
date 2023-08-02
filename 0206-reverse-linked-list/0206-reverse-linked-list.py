# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        if not head:
            return None
        while head.next!=None:
            stack.append(head)
            head=head.next
        i=head
        while len(stack)>0:
            i.next=stack.pop()
            i=i.next
        i.next=None
        return head
            
            