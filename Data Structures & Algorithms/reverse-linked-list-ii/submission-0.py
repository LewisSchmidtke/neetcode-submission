# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        left_node = None
        right_node = None

        curr = front = head
        count = 1
        prev_left = None
        while curr:
            if count == left:
                left_node = curr
            elif count == right:
                right_node = curr

            if count < left:
                prev_left = curr

            curr = curr.next
            count += 1

        dock = right_node.next
        right_node.next = None

        prev = dock
        curr = left_node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if prev_left is not None:
            prev_left.next = prev
        else:
            front = prev

        return front



