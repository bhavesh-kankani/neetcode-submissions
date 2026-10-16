# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = head = ListNode()
        while l1 and l2:
            summ = l1.val + l2.val + carry
            curr.next = ListNode(summ%10)
            carry = summ//10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            summ = l1.val + carry
            curr.next = ListNode(summ%10)
            carry = summ//10
            curr = curr.next
            l1 = l1.next
        while l2:
            summ = l2.val + carry
            curr.next = ListNode(summ%10)
            carry = summ//10
            curr = curr.next
            l2 = l2.next
        if carry != 0:
            curr.next = ListNode(carry)
        return head.next
