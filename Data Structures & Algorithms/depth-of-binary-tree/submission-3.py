# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ############# Top down approach #############
        # # if not root:
        # #     return 0

        # # depth = 1
        # # def calc_depth(root, counter):
        # #     if root is None:
        # #         return counter

        # #     counter += 1 # Because its not None we found another Node
        # #     left = calc_depth(root.left, counter)
        # #     right = calc_depth(root.right, counter)
        # #     counter = max(left, right)
        # #     return counter

        # # return max(calc_depth(root.left, depth), calc_depth(root.right, depth))

        # ############# Bottom up approach #############
        # if not root:
        #     return 0

        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return max(left, right) + 1

        if not root:
            return 0

        queue = deque()
        queue.append(root)

        level = 0
        while queue:
            for _ in range(len(queue)):
                curr_node = queue.popleft()

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            level += 1
        
        return level


