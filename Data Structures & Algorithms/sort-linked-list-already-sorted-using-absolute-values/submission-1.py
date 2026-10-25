# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortLinkedList(self, head: ListNode) -> ListNode:
        # extract negative value into separate LL and remove from initial list
        # add the negative LL to the front of the normal LL
        
        negLL = dummyN = ListNode()

        curr = head
        prev = dummyH = ListNode(0, head)
        while curr:
            temp = curr.next
            if curr.val < 0:
                prev.next = curr.next

                negLL.next = curr
                negLL = negLL.next
                negLL.next = None
            else:
                prev = curr # Only move prev pointer when positive or 0

            curr = temp

        p = dummyH.next
        c = dummyN.next
        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp

        return p
        

