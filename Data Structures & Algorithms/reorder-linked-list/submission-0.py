# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(r_head):
            prev = None
            while r_head:
                temp = r_head.next
                r_head.next = prev
                prev = r_head
                r_head = temp
            return prev

        # Find the mid element so that we reverse the right half
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid_head = slow

        # reverse the right half and merge both
        mid_head = reverse(mid_head)
        
        # merging the first half and second half
        curr = head
        while curr and mid_head:
            # print("before reordering", curr.val, mid_head.val)
            temp1 = curr.next
            temp2 = mid_head.next

            curr.next = mid_head
            if mid_head != temp1:
                mid_head.next = temp1
            else:
                mid_head.next = None

            curr = temp1
            mid_head = temp2
        
        # curr= head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next