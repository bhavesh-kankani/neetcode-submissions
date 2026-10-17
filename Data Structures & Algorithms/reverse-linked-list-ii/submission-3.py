# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        curr = head
        prev = None
        idx = 1
        while curr:
            if idx <= left:
                left_list = prev
                end_node = curr
            elif idx > left and idx < right:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                idx += 1
                continue
            elif idx == right:
                end_node.next = curr.next
                curr.next = prev
                if left_list:
                    left_list.next = curr
            else:
                break
            
            # iteration
            idx += 1
            prev = curr
            curr = curr.next
        return head if left != 1 else prev
        