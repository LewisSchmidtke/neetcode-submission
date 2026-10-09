# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # O(m+n) time but O(m+n) space
        # node_dict = {}

        # a_curr = headA
        # b_curr = headB

        # while b_curr:
        #     node_dict[b_curr] = 1
        #     b_curr = b_curr.next
        
        # while a_curr:
        #     if a_curr in node_dict:
        #         return a_curr
        #     node_dict[a_curr] = 1
        #     a_curr = a_curr.next

        # return None

        # Two pointer merge approach | O(m+n) time and O(1) space
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else headB
            pointer_b = pointer_b.next if pointer_b else headA

        # Will either be at the node where both lists link or point to None if they dont
        return pointer_a












