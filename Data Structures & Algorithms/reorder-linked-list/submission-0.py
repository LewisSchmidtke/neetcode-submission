# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # initial 0 -> 1 -> 2 -> 3
        # target 0 -> 3 -> 1 -> 2
        # Approach split, reverse, traverse
        # Split at mid point -> Find mid point through two pointer (fast, slow)
        # Reverse list after mid point
        # Traverse and connect while incrementing
        
        # Find mid with slow/fast pointers
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        second_list = mid.next
        mid.next = None # Define tail of first list

        # Reverse second list
        previous = None
        current = second_list
        while current:
            temp_next = current.next
            current.next = previous
            previous = current
            current = temp_next

        rev_second_list = previous

        # Merge
        first = head
        while rev_second_list:
            temp_1 = first.next
            temp_2 = rev_second_list.next
            first.next = rev_second_list
            rev_second_list.next = temp_1
            first = temp_1
            rev_second_list = temp_2
