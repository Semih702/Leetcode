# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root=head
        left=None
        while root:
            temp=root.next
            root.next=left
            left=root
            root=temp
        return left