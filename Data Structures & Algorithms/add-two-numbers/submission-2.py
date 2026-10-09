# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lead = l1
        head = lead
        ref = l2
        carries_one = False
        
        while lead and ref:
            new_val = lead.val + ref.val

            if carries_one:
                new_val += 1
                carries_one = False
            if new_val > 9:
                new_val = new_val - 10
                carries_one = True
            
            lead.val = new_val

            if not lead.next:
                if ref.next: # For the case that not ref.next but lead.next, we dont need to do anything as lead will be the longer LL anyway
                    lead.next = ref.next
                    return head
                # From here both lead.next and ref.next are None, meaning they have the same length total and we only need to check if there was an additional one that carried
                if carries_one: 
                    new_magnitude = ListNode(1, None)
                    lead.next = new_magnitude
                    return head

            lead = lead.next
            ref = ref.next

        return head
        



            

