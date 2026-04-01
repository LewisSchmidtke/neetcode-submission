class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        traverse = 0
        shift = 0

        while traverse < len(nums):
            if nums[traverse] > 0 and traverse % 2 == 0 or nums[traverse] < 0 and traverse % 2 != 0:
                pass
            else:
                shift = traverse
                if shift % 2 == 0:
                    while nums[shift] < 0:
                        shift += 1
                else:
                    while nums[shift] > 0:
                        shift += 1
                        
                temp = shift - 1
                while shift > traverse:
                    nums[temp], nums[shift] = nums[shift], nums[temp]
                    shift -= 1
                    temp -= 1

            traverse += 1

        return nums
            



            