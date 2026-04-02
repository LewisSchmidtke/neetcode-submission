# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        res = [] 

        while stack:
            curr, v = stack.pop(), visit.pop()
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    stack.append(curr.right)
                    stack.append(curr.left)
                    visit.append(True)
                    visit.append(False)
                    visit.append(False)

        return res
