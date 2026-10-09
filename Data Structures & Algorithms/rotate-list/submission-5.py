# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        # Find length of linked list O(n)
        ll_length = 1
        tail = head
        while tail.next:
            ll_length += 1
            tail = tail.next
        
        # adjust k to be in range [0, ll_lengt]
        adjusted_k = k % ll_length
        if adjusted_k == 0:
            return head
        
        new_front_element_index = ll_length - adjusted_k # Find pos index of new front element

        # Iterate up until we reach the new element, remove the next pointer from its previous node
        curr = head
        prev = None
        node_index = 0

        while curr:
            if node_index == new_front_element_index:
                prev.next = None # Remove pointer from prev node to new head
                tail.next = head # connect tail to head to complete linked list
                return curr
            prev = curr
            curr = curr.next
            node_index += 1
