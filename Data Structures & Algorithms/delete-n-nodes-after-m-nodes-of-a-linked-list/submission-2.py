# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        countN = 0

        while curr:
            countM = 0
            while curr and countM < m:
                countM += 1
                prev = curr
                curr = curr.next
                
            countN = 1
            while curr and countN < n:
                countN += 1
                curr = curr.next
            
            if not curr:
                prev.next = None
                break

            prev.next = curr.next
            curr = curr.next
            prev = curr
            

        return dummy.next            