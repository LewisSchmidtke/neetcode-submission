# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_dict = {}

        a_curr = headA
        b_curr = headB

        while b_curr:
            node_dict[b_curr] = 1
            b_curr = b_curr.next
        
        while a_curr:
            if a_curr in node_dict:
                return a_curr
            node_dict[a_curr] = 1
            a_curr = a_curr.next

        return None
