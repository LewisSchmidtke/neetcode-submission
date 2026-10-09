# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            return Node(insertVal)

        insert = Node(insertVal)
        inserted = False

        prev = None
        curr = head
        while not inserted:
            if (prev is not None and prev.val < insert.val < curr.val) or (prev is not None and prev.val == curr.val) :
                inserted = True
                prev.next = insert
                insert.next = curr
            else:
                prev = curr
                curr = curr.next

        return head
