class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation_map = {
            "0" : "0",
            "1" : "1",
            "6" : "9",
            "8" : "8",
            "9" : "6"
        }


        left = 0
        right = len(str(n)) - 1
        str_n = str(n)

        solution = [None] * len(str_n)

        while left <= right:
            if str_n[left] not in rotation_map or str_n[right] not in rotation_map:
                return False
            solution[left] = rotation_map[str_n[right]]
            solution[right] = rotation_map[str_n[left]]

            left += 1
            right -= 1

        new_number = int("".join(solution))
        
        return not new_number == n
        