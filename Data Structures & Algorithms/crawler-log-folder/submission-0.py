class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_stack = []
        folder_depth = 0

        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if folder_stack:
                    folder_stack.pop()
                    folder_depth -= 1
            else:
                folder_stack.append(log)
                folder_depth += 1

        return folder_depth