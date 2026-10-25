# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merge_start = None
        merge_end = None

        curr = head = list1
        prev = None
        count = 0
        while curr:
            if count == a:
                merge_start = prev
            
            if count == b:
                merge_end = curr.next
                break

            count += 1
            prev = curr
            curr = curr.next
        
        merge_start.next = list2

        curr = list2
        prev = None
        while curr:
            prev = curr
            curr = curr.next
        
        prev.next = merge_end

        return head


