class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        # Stack solution O(n) space and time
        # folder_stack = []

        # for log in logs:
        #     if log == "./":
        #         continue
        #     elif log == "../":
        #         if folder_stack:
        #             folder_stack.pop()
        #     else:
        #         folder_stack.append(log)

        # return len(folder_stack)

        # Counter solution O(n) time O(1) space
        folder_depth = 0

        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if folder_depth > 0:
                    folder_depth -= 1
            else:
                folder_depth += 1

        return folder_depth