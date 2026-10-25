# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # previous is new head
        temp = prev
        headN = prev.next
        prev = dummy = temp
        maxVal = prev.val

        while headN:
            if headN.val >= maxVal: # No bigger values in original list order after current node
                prev = headN
                maxVal = headN.val
            else:
                prev.next = headN.next
            
            headN = headN.next
        
        # Wrong order now but all relevant nodes removed
        curr = dummy
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev









