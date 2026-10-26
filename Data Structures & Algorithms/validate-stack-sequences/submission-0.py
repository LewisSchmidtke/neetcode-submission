class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        pusher = 0
        popper = 0

        while pusher < len(pushed) and popper < len(popped):
            if pushed[pusher] == popped[popper]:
                pusher += 1
                popper += 1
                continue
            
            if stack and popped[popper] == stack[-1]:
                popper += 1
                stack.pop()
                continue

            stack.append(pushed[pusher])
            pusher += 1
        
        while stack and popper < len(popped) and stack[-1] == popped[popper]:
            popper += 1
            stack.pop()
        
        return not len(stack) > 0 





