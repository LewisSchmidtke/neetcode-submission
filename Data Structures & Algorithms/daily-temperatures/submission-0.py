class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

    
        # reverse iterate over temperatures
        # Need a datatype to keep track of maximum temp and day of maximum temp (t, d)
        # First entry always the top element as most recent hot day -> stack []
        # if temperatures[i] is the highest we've seen -> we can empty the stack
        # Otherwise push temp and day tuple to stack
        # Compare current iteration to top element from stack -> if smaller push to stack, otherwise pop until we find max 
        
        results = [0] * len(temperatures)
        
        
        temp_stack = []
        
        for index, temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1][0]:
                stack_temp, stack_index = temp_stack.pop()
                results[stack_index] = index - stack_index

            temp_stack.append((temp, index))

        return results
