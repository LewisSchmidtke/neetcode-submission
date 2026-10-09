# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # n1 -> n2 -> n3 -> n4 -> None || None <- n1 <- n2 <- n3 <- n4

        # None <- n1 n2 -> n3... (previous = n1, current = n2)
        # temp next = n3, None <- n1 <- n2 n3 -> n4... (previous = n2, current = n3)
        # ...
        # current n4, previous n3  | None <- n1 <- n2 <- n3  n4 -> None
        # temp = None, | None <- n1 <- n2 <- n3 <- n4  None || previous = n4, current = None -> return previous


        # previous = None
        # current = head

        # while current:
        #     temp_next = current.next
        #     current.next = previous
        #     previous = current
        #     current = temp_next

        # return previous


        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head
        
