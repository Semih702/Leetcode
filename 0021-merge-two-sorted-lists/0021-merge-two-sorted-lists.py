# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        iterr= ListNode()
        dummy=iterr

        while list1 and list2:
            if list1.val<list2.val:
                iterr.next=list1
                list1=list1.next
            else:
                iterr.next=list2
                list2=list2.next
            iterr=iterr.next
        if list1:
            iterr.next=list1
        if list2:
            iterr.next=list2
        return dummy.next
            
            
            