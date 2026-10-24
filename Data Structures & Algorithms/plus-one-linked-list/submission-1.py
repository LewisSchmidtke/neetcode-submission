# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        curr = new_head = self.revLL(head)
        prev = None


        initialOperation = 1
        carryOne = 0
        while curr:
            prev = curr
            new_value = curr.val + initialOperation + carryOne
            initialOperation = 0

            if new_value < 10:
                curr.val = new_value
                carryOne = 0
                break

            carryOne = 1
            curr.val = 0    
            curr = curr.next
        
        if carryOne > 0:
            prev.next = ListNode(1, None)
        
        return self.revLL(new_head)


        
    def revLL(self, h):
        p = None
        c = h

        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp
        
        return p