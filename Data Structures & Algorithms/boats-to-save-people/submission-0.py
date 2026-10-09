class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = sorted(people)

        left = 0
        right = len(sorted_people) - 1

        min_boats = 0

        while left <= right:
            combination = sorted_people[right] + sorted_people[left]
            if combination > limit:
                min_boats += 1
                right -= 1
            else:
                min_boats += 1
                right -= 1
                left += 1
        
        return min_boats