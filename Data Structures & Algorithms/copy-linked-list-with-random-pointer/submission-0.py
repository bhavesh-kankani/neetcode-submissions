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
        if head is None: return None
        # store random pointers indices
        og_curr = head
        idx = 0
        indices = {}
    
        while og_curr:
            indices[og_curr] = idx
            idx += 1
            og_curr = og_curr.next
        indices[None] = None

        # create copy of linkedlist
        copy = prev = Node(0)
        d = {}
        idx = 0
        og_curr = head
        while og_curr:
            curr = Node(og_curr.val)
            d[idx] = curr
            idx += 1
            prev.next = curr

            og_curr = og_curr.next
            prev = curr # prev points to curr, curr creates new node in nxt iter
        d[None] = None

        # random pointers
        copy = copy.next
        curr = copy
        og_curr = head
        while og_curr:
            idx = indices[og_curr.random]
            curr.random = d[idx]

            og_curr = og_curr.next
            curr = curr.next
        return copy



        