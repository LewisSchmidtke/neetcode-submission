class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1

        traverse = 0

        # Negative numbers at odd indices
        # Positive numbers at even indices

        while traverse < len(nums):
            numb = nums[traverse]
            is_gr_0 = numb > 0 # if true, should be at even pos, else odd pos

            if is_gr_0 and traverse % 2 == 0 or not is_gr_0 and traverse % 2 != 0:
                print(numb)
                if traverse % 2 == 0:
                    even += 2
                else:
                    odd += 2

                traverse += 1
                continue

            if is_gr_0: # traverse 1, even 2, odd 1
                while nums[even] > 0:
                    even += 2

                nums[traverse], nums[even] = nums[even], nums[traverse]

            else:
                while nums[odd] < 0:
                    odd += 2
                nums[traverse], nums[odd] = nums[odd], nums[traverse]

        return nums
            



            