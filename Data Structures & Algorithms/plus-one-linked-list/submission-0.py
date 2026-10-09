# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        prevs = [None]
        curr = head

        while curr:
            prevs.append(curr)
            curr = curr.next
        
        finished = False

        prev_point = len(prevs) - 1
        carries = 0

        while prev_point >= 0:
            if prev_point == 0:
                if carries > 0:
                    node = ListNode(1, head)
                    head = node

                return head

            if prev_point == len(prevs) - 1:
                res = prevs[prev_point].val + 1 # +1 from task description
            else:
                res = prevs[prev_point].val + carries

            carries = 0

            if res == 10:
                carries = 1
                prevs[prev_point].val = 0
                prev_point -= 1

            else:
                prevs[prev_point].val = res
                return head

