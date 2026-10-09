# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find length of linked list O(n)
        ll_length = 0
        curr = head
        while curr:
            ll_length += 1
            if curr.next is None:
                break
            curr = curr.next
        
        # adjust k to be in range [0, ll_lengt]
        adjusted_k = k % ll_length
        # Index of new front element can be calculated:
        new_front_element_index = ll_length - adjusted_k

        # Point the last element in ll to have the head of the current linked list as
        last_element = curr

        # Iterate up until we reach the new element, remove the next pointer from its previous node
        curr = head
        prev = None
        node_index = 0

        while curr:
            if node_index == new_front_element_index:
                prev.next = None
                last_element.next = head
                return curr
            prev = curr
            curr = curr.next
            node_index += 1
