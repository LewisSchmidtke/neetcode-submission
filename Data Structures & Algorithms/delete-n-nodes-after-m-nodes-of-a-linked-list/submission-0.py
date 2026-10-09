# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        curr = head
        prev = None
        counter = 1
        skips = n
        while curr:
            if counter > m:
                skips = n
                while skips > 0 and curr:
                    curr = curr.next
                    skips -= 1

                prev.next = curr
                counter = 1

            counter += 1
            prev = curr
            if curr:
                curr = curr.next
            else:
                break

        return head