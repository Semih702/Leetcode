"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap={}
        start=Node(0)
        left=start
        while head:
            temp=hashmap.get(head)
            
            if not temp:
                hashmap[head]=Node(head.val,head.next,head.random)
            
            left.next=hashmap[head]
            head=head.next
            left=left.next
        left=start
        while left:
            left.random=hashmap.get(left.random)
            left=left.next
        return start.next