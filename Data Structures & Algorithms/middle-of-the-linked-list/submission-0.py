# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two pointer approach Slow/Fast
        slow = head
        fast = head.next

        while fast:
            slow = slow.next
            if not fast.next or not fast.next.next:
                break
            fast = fast.next.next

        return slow