# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        left=slow.next
        slow.next=None

        prev=None
        while left:
            temp=left.next
            left.next=prev
            prev=left
            left=temp
        iterr=head
        while iterr and prev:
            temp=iterr.next
            temp2=prev.next
            iterr.next=prev
            prev.next=temp
            iterr=temp
            prev=temp2