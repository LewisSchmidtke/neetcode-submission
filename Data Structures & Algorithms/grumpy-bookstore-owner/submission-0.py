class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        baseline_satisfied = sum([k if grumpy[index] == 0  else 0 for index, k in enumerate(customers)]) # O(n) with n being length customers, length grumpy 
        
        res = 0

        left = 0
        right = 0
        window_satisfied = 0
        while right < len(customers):

            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    window_satisfied -= customers[left]
                left += 1

            if grumpy[right] == 1:
                window_satisfied += customers[right] 

            right += 1
            res = max(res, window_satisfied)

        return res + baseline_satisfied

        # window_satisfied = sum([k if grumpy[index] == 1  else 0 for index, k in enumerate(customers[left:right + 1])])
        # left += 1
        # right += 1
        # while right < len(customers):
        #     if grumpy[left - 1] == 1:
        #         window_satisfied -= customers[left]
        #     if grumpy[right] == 1:
        #         window_satisfied += customers[right]
            
        #     left += 1
        #     right += 1
        #     res = max(res, window_satisfied)

        # return res + baseline_satisfied





        
