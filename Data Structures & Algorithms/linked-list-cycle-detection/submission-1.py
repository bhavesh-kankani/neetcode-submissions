# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head and head.val != 2000:
            if head.val == 2000:
                return True
            head.val = 2000
            head = head.next
        return head.val == 2000 if head else False