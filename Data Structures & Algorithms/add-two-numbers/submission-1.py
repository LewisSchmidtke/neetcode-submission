# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_point = l1
        l2_point = l2
        counter = 0
        carries_one = False

        lead, ref = (l2, l1) if len_l2 >= len_l1 else (l1, l2)
        head = lead

        while lead:
            if counter < magnitude_index:
                lead = lead.next
                counter += 1
                continue
            new_val = lead.val + ref.val
            if carries_one:
                new_val += 1
                carries_one = False
            if new_val > 9:
                new_val = new_val - 10
                carries_one = True
            
            lead.val = new_val
            if not lead.next:
                break
            lead = lead.next
            ref = ref.next

        if carries_one:
            lead.next = ListNode(1, None)
        
        return head


        lead = l1
        ref = l2
        carries_one = False
        
        while lead and ref:
            new_val = lead.val + ref.val
            
            

