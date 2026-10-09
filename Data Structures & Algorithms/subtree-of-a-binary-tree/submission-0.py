# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        r_str = self.convert(root)
        sr_str = self.convert(subRoot)

        left = 0
        right = 0 # Starting at first number
        count = 0
        print(r_str, sr_str)

        while left < len(r_str) and right < len(sr_str):
            if r_str[left] != sr_str[right]:
                count = 0
                right = 0
                left += 1
                continue

            while left < len(r_str) and right < len(sr_str) and r_str[left] == sr_str[right]:

                left += 1
                right += 1
                count += 1

                if count == len(sr_str):
                    return True
        
        if count == len(r_str):
            return True
        
        return False


    def convert(self, r):
        if r is None:
            return "$-"
        else:
            return "$" + str(r.val) + self.convert(r.left) + self.convert(r.right)